from pycparser import c_ast, parse_file

import sys

FILENAME = "sqr_array_1.c"

requirements = {
			"int_array": {
				"text": "int-Array der Größe 10",
				"checked": False
			}
		}

def check_exercise(filename):
	global requirements

	ast = parse_file(filename, use_cpp=True, cpp_path="gcc", cpp_args=["-nostdinc", "-E", r"-Ipycparser/utils/fake_libc_include"])

	requirements["int_array"]["checked"] = True
	try:
		int_array = next(x for x in ast.ext if type(x) == c_ast.Decl and type(x.type) == c_ast.ArrayDecl and x.type.type.type.names == ["int"] and x.type.dim.value == "10")
	except StopIteration:
		requirements["int_array"]["checked"] = False

	if not requirements["int_array"]["checked"]:
		main_ast = next(x for x in ast.ext if type(x) == c_ast.FuncDef and x.decl.name == "main")

		requirements["int_array"]["checked"] = True
		try:
			int_array = next(x for x in main_ast.body.block_items if type(x) == c_ast.Decl and type(x.type) == c_ast.ArrayDecl and x.type.type.type.names == ["int"] and x.type.dim.value == "10")
		except StopIteration:
			requirements["int_array"]["checked"] = False

if __name__ == "__main__":
	check_exercise(FILENAME)

	failure = False

	for r in requirements.values():
		if r["checked"]:
			print("[X] ", end="")
		else:
			print("[ ] ", end="")
			failure = True
		print(r["text"])

	if failure:
		sys.exit(1)

