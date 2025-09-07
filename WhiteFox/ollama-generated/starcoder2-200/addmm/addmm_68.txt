
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1=None): 
        v0 = torch.randn(256) 
        v1  = torch.randn(32) 
        v2  = torch.zeros(32) 
        return v0 + v1 + v2 
 
m  = Model()


