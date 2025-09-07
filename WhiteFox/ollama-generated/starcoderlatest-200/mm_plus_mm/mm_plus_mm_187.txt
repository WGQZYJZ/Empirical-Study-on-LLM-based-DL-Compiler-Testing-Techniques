
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.MMSE()
 
    def forward(self, x1, x2, x3, x4):
        v1  = self.mm(x1, x2)
        v2  = self.mm(x3, x4)
        v3  = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 64, 64)
x2 = torch.randn(8, 64, 64)
x3 = torch.randn(8, 64, 64)
x4 = torch.randn(8, 64, 64)
