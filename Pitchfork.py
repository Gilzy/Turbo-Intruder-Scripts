#the first request will place the first payload from payload set 1 into position 1 and the first payload from payload set 2 into position 2; the second request will place the second payload from payload set 1 into position 1 and the second payload from payload set 2 into position 2, etc. 

# Find more example scripts at https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    filenames = ['path\to\file1.txt', 'path\to\file2.txt']

    def gen_line(filename):
        with open(filename) as f:
            for line in f:
                yield line.strip()

    gens = [gen_line(n) for n in filenames]

    for file1_line, file2_line in zip(*gens):
        engine.queue(target.req, [file1_line.rstrip(), file2_line.rstrip()])


def handleResponse(req, interesting):
    if interesting: #to show only responses with code 200 in results table change this line to "if '200 OK' in req.response:"
        table.add(req)
