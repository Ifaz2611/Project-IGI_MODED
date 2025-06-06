from . import check


def register_parser(cli):
	cmd = cli.add_parser('mef')
	sub = cmd.add_subparsers()
	sub.require = True

	sub_check = sub.add_parser('check')
	sub_check.add_argument('src', help="Source folder")
	sub_check.set_defaults(func=check.func)
