from pycparser import c_ast, parse_file

import sys

FILENAME = "temperaturen.c"

class ExerciseChecker(c_ast.NodeVisitor):
	def __init__(self):
		self.number_of_for_loops = 0
		self.number_of_while_loops = 0
		self.errors = []
		super()

	def visit_For(self, node):
		self.errors.append("Zeile %d: Das Programm sollte keine for-Schleifen enthalten." % node.coord.line)

	def visit_While(self, node):
		self.number_of_while_loops += 1
		if self.number_of_while_loops > 1:
			self.errors.append("Zeile %d: Das Programm sollte nur eine while-Schleife enthalten." % node.coord.line)

	def visit_Decl(self, node):
		if type(node.type) != c_ast.FuncDecl:
			for name in node.type.type.names:
				if name != "int":
					self.errors.append("Zeile %d: Das Programm sollte nur int-Variablen verwenden." % node.coord.line)

def check_exercise(filename):
	errors = []

	ast = parse_file(filename, use_cpp=True, cpp_path="gcc", cpp_args=["-nostdinc", "-E", r"-Ipycparser/utils/fake_libc_include"])

	v = ExerciseChecker()
	main_ast = next(x for x in ast.ext if type(x) == c_ast.FuncDef and x.decl.name == "main")
	v.visit(main_ast)

	if v.number_of_while_loops == 0:
		v.errors.append("Das Programm sollte eine while-Schleife enthalten.")

	return v.errors

if __name__ == "__main__":
	errors = check_exercise(FILENAME)
	for error in errors:
		print("-", error)
	if len(errors) > 0:
		sys.exit(1)

