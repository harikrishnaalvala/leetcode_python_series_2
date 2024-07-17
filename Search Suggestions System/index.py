class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ret = []
        for i in range(1, len(searchWord) + 1):
            j=bisect_left(products, searchWord[:i])
            ret.append([x for x in products[j:j+3] if x.startswith(searchWord[:i])])
        return ret
