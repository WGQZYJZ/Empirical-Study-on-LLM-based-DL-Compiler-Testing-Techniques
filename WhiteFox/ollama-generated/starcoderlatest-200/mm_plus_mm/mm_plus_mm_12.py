
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Conv2d(3, 8, 1)
        self.m2 = torch.nn.Conv2d(8, 16, 1)
 
    def forward(self, x1, x2):
        v1 = self.m1(x1)
        v2 = self.m2(v1)
        v3 = torch.mm(v2, v2.t()) + torch.mm(v2, v2.t())  # Addition of the results of two matrix multiplications
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
