from pycparser import c_ast, parse_file

import sys

FILENAME = "swap.c"

requirements = {
			"function_swap": {
				"text": "Funktion swap: int* X int* -> void",
				"checked": False
			}
		}

def check_exercise(filename):
	ast = parse_file(filename, use_cpp=True, cpp_path="gcc", cpp_args=["-nostdinc", "-E", r"-Ipycparser/utils/fake_libc_include"])

	requirements["function_swap"]["checked"] = True
	try:
		func_swap = next(x for x in ast.ext if type(x) == c_ast.FuncDef and x.decl.name == "swap" and x.decl.type.type.type.names == ["void"] and len(x.decl.type.args.params) == 2 and len([p for p in x.decl.type.args.params if type(p.type) == c_ast.PtrDecl and p.type.type.type.names == ["int"]]) == 2)
	except StopIteration:
		requirements["function_swap"]["checked"] = False

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

