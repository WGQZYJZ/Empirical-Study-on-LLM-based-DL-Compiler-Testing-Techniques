
class Model(torch.nn.Module):
    def __init__(self, list1=[], list2=[]):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1[0], x1[1])
        v2 = torch.cat([v1] * len(list2))
