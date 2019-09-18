import urllib.request, urllib.parse, urllib.error
from collections import deque
home='http://secon.utulsa.edu/cs2123/webtraverse/index.html'
alink='http://secon.utulsa.edu/cs2123/webtraverse/alink.html'
blink='http://secon.utulsa.edu/cs2123/webtraverse/blink.html'
clink='http://secon.utulsa.edu/cs2123/webtraverse/clink.html'
dijkstra='http://secon.utulsa.edu/cs2123/webtraverse/dijkstra.html'
turing="http://secon.utulsa.edu/cs2123/webtraverse/turing.html"
wainwright="http://secon.utulsa.edu/cs2123/webtraverse/wainwright.html"
king="https://secon.utulsa.edu/cs2123/webtraverse/kings.html"
bletchely="https://secon.utulsa.edu/cs2123/webtraverse/bletchley.html"
levelpage4="https://secon.utulsa.edu/cs2123/webtraverse/p4.html"
levelpage5="https://secon.utulsa.edu/cs2123/webtraverse/p5.html"
levelpage5b='https://secon.utulsa.edu/cs2123/webtraverse/p5b.html'
levelpage6="https://secon.utulsa.edu/cs2123/webtraverse/p6.html"
levelpage7="https://secon.utulsa.edu/cs2123/webtraverse/p7.html"
levelpage8="https://secon.utulsa.edu/cs2123/webtraverse/p6.html"


G={home:[alink,blink,clink],
   alink:[dijkstra,turing,wainwright,home],
   dijkstra:[turing],
   turing:[king],
   king:[turing,bletchely],
   bletchely:[turing],
   blink:[levelpage4,levelpage5,home],
   levelpage5:[levelpage5b],
   levelpage5b:[turing],
   clink:[levelpage6,levelpage7,blink,home],
   levelpage6:[levelpage8],
   levelpage8:[alink],
   levelpage7:[clink]
}

def byte2str(b):
    """
    Input: byte sequence b of a string
    Output: string form of the byte sequence
    Required for python 3 functionality
    """
    return "".join(chr(a) for a in b)


def getLinks(url, baseurl="http://secon.utulsa.edu/cs2123/webtraverse/"):
    """
    Input: url to visit, Boolean absolute indicates whether URLs should include absolute path (default) or not
    Output: list of pairs of URLs and associated text
    """
    # import the HTML parser package
    try:
        from bs4 import BeautifulSoup
    except:
        print('You must first install the BeautifulSoup package for this code to work')
        raise
    # fetch the URL and load it into the HTML parser
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), features="html.parser")
    # pull out the links from the HTML and return
    return [baseurl + byte2str(a["href"].encode('ascii', 'ignore')) for a in soup.findAll('a')]


def print_dfs(url):
    S, Q = set(), []  # Visited-set and queue
    Q.append(s)  # We plan on visiting s
    while Q:  # Planned nodes left?
        u = Q.pop()  # Get one
        if u in S: continue  # Already visited? Skip it
        S.add(u)  # We've visited it now
        Q.extend(G[u])  # Schedule all neighbors
        yield u
    """
    Print all links reachable from a starting **url**
    in depth-first order
    """
    #


def print_bfs(url):
    """
    Print all links reachable from a starting **url**
    in breadth-first order
    """
    #


def find_shortest_path(url1, url2):
    """
    Find and return the shortest path
    from **url1** to **url2** if one exists.
    If no such path exists, say so.
    """
    #


def find_max_depth(start_url):
    """
    Find and return the URL that is the greatest distance from start_url, along with the sequence of links that must be followed to reach the page.
    For this problem, distance is defined as the minimum number of links that must be followed from start_url to reach the page.
    """
    #


if __name__ == "__main__":
    starturl = "http://secon.utulsa.edu/cs2123/webtraverse/index.html"
    print("*********** (a) Depth-first search   **********")
    print_dfs(starturl)
    print("*********** (b) Breadth-first search **********")
    print_bfs(starturl)
    print("*********** (c) Find shortest path between two URLs ********")
    find_shortest_path("http://secon.utulsa.edu/cs2123/webtraverse/index.html",
                       "http://secon.utulsa.edu/cs2123/webtraverse/wainwright.html")
    find_shortest_path("http://secon.utulsa.edu/cs2123/webtraverse/turing.html",
                       "http://secon.utulsa.edu/cs2123/webtraverse/dijkstra.html")
    print("*********** (d) Find the longest shortest path from a starting URL *****")
    find_max_depth(starturl)

