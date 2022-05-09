from pycparser import c_ast, parse_file

import sys

FILENAME = "sqr_array_2.c"

requirements = {
			"int_array": {
				"text": "int-Array der Größe 10",
				"checked": False
			},
			"func_rev_print": {
				"text": "Funktion rev_print: int* -> void",
				"checked": False
			},
			"func_rev_print_call": {
				"text": "Aufruf von rev_print durch main mit dem int-Array als Parameter",
				"checked": False
			}
		}

def check_exercise(filename):
	global requirements

	ast = parse_file(filename, use_cpp=True, cpp_path="gcc", cpp_args=["-nostdinc", "-E", r"-Ipycparser/utils/fake_libc_include"])
	main_ast = next(x for x in ast.ext if type(x) == c_ast.FuncDef and x.decl.name == "main")

	requirements["int_array"]["checked"] = True
	try:
		int_array = next(x for x in ast.ext if type(x) == c_ast.Decl and type(x.type) == c_ast.ArrayDecl and x.type.type.type.names == ["int"] and x.type.dim.value == "10")
		requirements["int_array"]["name"] = int_array.name
	except StopIteration:
		requirements["int_array"]["checked"] = False

	if not requirements["int_array"]["checked"]:
		requirements["int_array"]["checked"] = True
		try:
			int_array = next(x for x in main_ast.body.block_items if type(x) == c_ast.Decl and type(x.type) == c_ast.ArrayDecl and x.type.type.type.names == ["int"] and x.type.dim.value == "10")
			requirements["int_array"]["name"] = int_array.name
		except StopIteration:
			requirements["int_array"]["checked"] = False

	requirements["func_rev_print"]["checked"] = True
	try:
		func_f = next(x for x in ast.ext if type(x) == c_ast.FuncDef and x.decl.name == "rev_print" and x.decl.type.type.type.names == ["void"] and len(x.decl.type.args.params) == 1 and len([p for p in x.decl.type.args.params if type(p.type) == c_ast.PtrDecl and p.type.type.type.names == ["int"]]) == 1)
	except StopIteration:
		requirements["func_rev_print"]["checked"] = False
			
	if requirements["int_array"]["checked"] and requirements["func_rev_print"]["checked"]:
		requirements["func_rev_print_call"]["checked"] = True
		try:
			func_f = next(x for x in main_ast.body.block_items if type(x) == c_ast.FuncCall and x.name.name == "rev_print" and ((type(x.args.exprs[0]) == c_ast.ID and x.args.exprs[0].name == requirements["int_array"]["name"]) or (type(x.args.exprs[0]) == c_ast.UnaryOp and x.args.exprs[0].op == "&" and type(x.args.exprs[0].expr) == c_ast.ArrayRef and x.args.exprs[0].expr.name.name == requirements["int_array"]["name"] and x.args.exprs[0].expr.subscript.value == "0")))
		except StopIteration:
			requirements["func_rev_print_call"]["checked"] = False

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

