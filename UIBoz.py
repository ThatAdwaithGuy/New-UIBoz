

'''
psedo-code

a = DrawBoz([DrawBoz.AddText(f"Heelo {MyDynamicValue}")])

'''


def PageCounter(PageDict):
    if not PageDict:
        latest_key = 1
    else:
        # Find the latest key by converting keys to integers and taking the max
        latest_key = max(map(int, PageDict.keys()))
        # Increment the latest key by 1
        latest_key += 1
    return latest_key

PageDict = {}

class Page:
    def __init__(self, PageContent: DrawBoz, PageID: int=PageCounter(PageDict), PageName: str='Main Page') -> None:
        PageDict[PageID] = PageName
        self.Page = Page
        self.RenderedPage = PageContent.RenderString()

    def Refresh(self):
        print('\033c')

    def Print(self):
        print(self.RenderedPage)
