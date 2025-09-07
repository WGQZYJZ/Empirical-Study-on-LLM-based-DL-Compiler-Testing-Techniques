
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + 3
        v3 = F.relu6(v2)
        v4 = F.hardtanh_(v3, 0, 6)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(257,)
__output__  = m(x1)
