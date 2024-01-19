def findDuplicate(self, paths: List[str]) -> List[List[str]]:
    D = defaultdict(list)
    for path in paths:
        directory, *files = path.split()
        for file in files:
            filename, content = file.split('(')
            D[content].append(directory + '/' + filename)
    return [paths for paths in D.values() if len(paths) > 1]