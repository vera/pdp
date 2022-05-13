from pycparser import c_ast, parse_file

from functools import reduce

import sys

FILENAME = "long_long_bytes.c"

requirements = {
			"long_long": {
				"text": "long long-Variable mit Wert 0x1a1b2a2b3a3b4a4b",
				"checked": False
			},
			"unsigned_short_pointers": {
				"text": "vier unsigned short-Pointer-Variablen (-> 2 Bytes)",
				"checked": False
			},
			"long_long_printf": {
				"text": "long long-Variable mit %llx über printf ausgegeben",
				"checked": False
			},
			"unsigned_short_pointers_printf": {
				"text": "vier Doppelbytes über printf ausgegeben",
				"checked": False
			}
		}
		
def find_local_or_global(local_ast, global_ast, find_function, up_to_num=1):
	found = []

	global_it = (x for x in global_ast if find_function(x))
	while len(found) < up_to_num:
		try:
			ast_element = next(global_it)
			if ast_element.name not in found:
				found.append(ast_element.name)
		except StopIteration:
			break

	local_it = (x for x in local_ast if find_function(x))
	while len(found) < up_to_num:
		try:
			ast_element = next(local_it)
			if ast_element.name not in found:
				found.append(ast_element.name)
		except StopIteration:
			break

	if up_to_num == 1:
		return found[0] if found else None
	else:
		return found

def check_exercise(filename):
	global requirements

	ast = parse_file(filename, use_cpp=True, cpp_path="gcc", cpp_args=["-nostdinc", "-E", r"-Ipycparser/utils/fake_libc_include"])
	main_ast = next(x for x in ast.ext if type(x) == c_ast.FuncDef and x.decl.name == "main")
	
	long_long_name = find_local_or_global(main_ast.body.block_items, ast.ext, lambda x: type(x) == c_ast.Decl and type(x.type) == c_ast.TypeDecl and x.type.type.names == ["long", "long"] and x.init.value == "0x1a1b2a2b3a3b4a4bULL")
	if long_long_name:
		requirements["long_long"]["checked"] = True
		requirements["long_long"]["name"] = long_long_name
	
	unsigned_short_pointers_names = find_local_or_global(main_ast.body.block_items, ast.ext, lambda x: type(x) == c_ast.Decl and type(x.type) == c_ast.PtrDecl and x.type.type.type.names == ["unsigned", "short"], 4)
	if len(unsigned_short_pointers_names) == 4:
		requirements["unsigned_short_pointers"]["checked"] = True
		requirements["unsigned_short_pointers"]["name"] = unsigned_short_pointers_names
		
	if requirements["long_long"]["checked"]:
		long_long_printf = find_local_or_global(main_ast.body.block_items, [], lambda x: type(x) == c_ast.FuncCall and x.name.name == "printf" and "%llx" in x.args.exprs[0].value and reduce(lambda a, x: a or type(x) == c_ast.ID and x.name == requirements["long_long"]["name"], x.args.exprs, False))
		if long_long_printf:
			requirements["long_long_printf"]["checked"] = True

	if requirements["unsigned_short_pointers"]["checked"]:
		requirements["unsigned_short_pointers_printf"]["checked"] = True
		for ptr_name in requirements["unsigned_short_pointers"]["name"]:
			ptr_printf = find_local_or_global(main_ast.body.block_items, [], lambda x: type(x) == c_ast.FuncCall and x.name.name == "printf" and reduce(lambda a, x: a or (type(x) == c_ast.UnaryOp and x.op == "*" and x.expr.name == ptr_name), x.args.exprs, False))
			if not ptr_printf:
				requirements["unsigned_short_pointers_printf"]["checked"] = False
				break

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

