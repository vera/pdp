from pycparser import c_ast, parse_file

import sys

FILENAME = "global.c"

requirements = {
			"global_y": {
				"text": "globale Variable 'y' vom Typ int",
				"checked": False
			},
			"function_f": {
				"text": "Funktion f: int X int -> int",
				"checked": False
			},
			"local_x": {
				"text": "lokale Variable x der main-Funktion mit dem Typ int und dem Initialwert 4",
				"checked": False
			}
		}

def check_exercise(filename):
	global requirements

	ast = parse_file(filename, use_cpp=True, cpp_path="gcc", cpp_args=["-nostdinc", "-E", r"-Ipycparser/utils/fake_libc_include"])

	requirements["global_y"]["checked"] = True
	try:
		global_y = next(x for x in ast.ext if type(x) == c_ast.Decl and x.name == "y" and x.type.type.names == ["int"])
	except StopIteration:
		requirements["global_y"]["checked"] = False

	requirements["function_f"]["checked"] = True
	try:
		func_f = next(x for x in ast.ext if type(x) == c_ast.FuncDef and x.decl.name == "f" and x.decl.type.type.type.names == ["int"] and len(x.decl.type.args.params) == 2 and len([p for p in x.decl.type.args.params if p.type.type.names == ["int"]]) == 2)
	except StopIteration:
		requirements["function_f"]["checked"] = False
		
	main_ast = next(x for x in ast.ext if type(x) == c_ast.FuncDef and x.decl.name == "main")

	requirements["local_x"]["checked"] = True
	try:
		local_x = next(x for x in main_ast.body.block_items if type(x) == c_ast.Decl and x.name == "x" and x.type.type.names == ["int"] and x.init.value == "4")
	except StopIteration:
		requirements["local_x"]["checked"] = False

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

