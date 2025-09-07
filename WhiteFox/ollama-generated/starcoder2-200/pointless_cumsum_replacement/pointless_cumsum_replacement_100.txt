
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
       ...
        return v2

m = Model()
__output__  = m(torch.randn(30))

