from pycparser import c_ast, parse_file

import sys

FILENAME = "while1.c"

class ExerciseChecker(c_ast.NodeVisitor):
	def __init__(self):
		self.number_of_for_loops = 0
		self.number_of_while_loops = 0
		super()

	def visit_For(self, node):
		self.number_of_for_loops += 1

	def visit_While(self, node):
		self.number_of_while_loops += 1

def check_exercise(filename):
	errors = []

	ast = parse_file(filename, use_cpp=True, cpp_path="gcc", cpp_args=["-nostdinc", "-E", r"-Ipycparser/utils/fake_libc_include"])

	v = ExerciseChecker()
	v.visit(ast)
	if v.number_of_for_loops != 0:
		errors.append("Das Programm sollte keine for-Schleifen enthalten.")
	if v.number_of_while_loops != 3:
		errors.append("Das Programm sollte genau drei while-Schleifen enthalten.")
		
	return errors

if __name__ == "__main__":
	errors = check_exercise(FILENAME)
	for error in errors:
		print("-", error)
	if len(errors) > 0:
		sys.exit(1)

