
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2 = torch.sigmoid(v1) 
        return v2


m = Model()

x1 = torch.randn(50,3)
__output__= m(x1)