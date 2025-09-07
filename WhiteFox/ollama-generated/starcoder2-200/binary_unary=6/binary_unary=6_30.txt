
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        v3 = F.relu(v2) # or torch.nn.functional.relu()
        return v3

m = Model()

x1  = torch.randn(1, 32)
__output__  = m(x1)

