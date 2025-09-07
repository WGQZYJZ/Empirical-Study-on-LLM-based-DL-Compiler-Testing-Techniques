

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


m  = Model()
x1 = torch.randn(5, 3 * 64 * 64)
__output__  = m(x1)