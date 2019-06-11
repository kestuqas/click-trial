import click


@click.command()
@click.option('--string', default='CLICK', 
			  help="This is some great hel for you, isn't it?")
@click.option('--repeat', default=1,
			  help="This is how many time it will anoyingly repeat")
@click.argument('out', type=click.File('w'), default='-',
				required=False)

def cli(string, repeat, out):
	""" Bla bla bla"""
	click.echo(out)
	for x in xrange(repeat):
		click.echo("This is the %s trial" % string, file=out)