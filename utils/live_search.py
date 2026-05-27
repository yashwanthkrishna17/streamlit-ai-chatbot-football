from duckduckgo_search import DDGS

def web_search(q):

    out=[]

    with DDGS() as ddgs:

        results=ddgs.text(
            q + " football",
            max_results=5
        )

        for r in results:

            out.append(
                r["body"]
            )

    return "\n".join(out)