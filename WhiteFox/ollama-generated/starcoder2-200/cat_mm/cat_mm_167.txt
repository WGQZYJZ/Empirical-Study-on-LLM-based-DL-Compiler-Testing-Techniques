
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1):
        v0 = torch.mm(x1,y1)
        v1  = torch.cat([v0 for _ in range(5)]) 
        return v1

m  = Model()
x1 = torch.randn(4,20000)
y1 = torch.randn(20000,300)

