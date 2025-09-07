
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1 = torch.nn.Linear(3, 8)
        self.mm2 = torch.nn.Linear(64, 512)
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2) # Matrix multiplication between input1 and input2
        v2 = torch.mm(x3, x4) # Matrix multiplication between input3 and input4
        v3 = v1 + v2  # Addition of the results of the two matrix multiplications
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
x2 = torch.randn(8, 3)
x3 = torch.randn(16, 512)
x4 = torch.randn(256, 64)
