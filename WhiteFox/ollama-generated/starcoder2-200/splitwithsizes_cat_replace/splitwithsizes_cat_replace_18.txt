
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.splitwithsizes  = torch.nn.SplitWithSizes([1,4])
 
    def forward(self, x1):
        v2  = self.splitwithsizes(x1) 
        v3  = torch.cat(v2, dim=0)
        return v3
 
m  = Model()
x1  = torch.randn(8,)
