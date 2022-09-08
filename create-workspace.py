#!/bin/python3

import sys
import os


def main():

    workspacePath = '/home/codazoa/school/workspaces/'

    path = os.path.abspath(os.getcwd())
    name = ''

    if len(sys.argv) < 2:
        print('Please provide workspace NAME')
        print('create-workspace NAME [PATH]')
        exit()

    if len(sys.argv) == 3:
        path = sys.argv[2]

    name = sys.argv[1]

    # create folder at path
    path = os.path.join(path, name)

    os.mkdir(path, 0o755)
    print(f'Directory {path} created')

    with open(path+'/issues.md', 'w+') as issueFile:
        issueFile.write("## Resolved Issues ##\n\n\n\n## Open Issues ##\n")

    # create workspace file in workspacePath
    workspacePath = os.path.join(workspacePath, name + '.code-workspace')

    with open(workspacePath, 'w+') as workFile:
        workFile.write(
        """{
	"folders": [
		{
			"path": "%s"
		}
	],
	"settings": {}
}
        """ % path)


    os.system('codium %s' % workspacePath)

    pass

if __name__ == '__main__':
    main()