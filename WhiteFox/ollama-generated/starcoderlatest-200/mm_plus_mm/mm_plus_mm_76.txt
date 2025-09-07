
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.nn.Linear(256, 8)
        self.mat2 = torch.nn.Linear(128, 32)
 
    def forward(self, x1, x2, x3):
        v1 = self.mat1(x1)
        v2 = self.mat2(x2)
        v3 = torch.mm(v1, v2)
        v4 = v3 + x3
        return v4

# Initializing the model
m = Model()

 # Inputs to the model
__input1__ = torch.randn(50, 256)
__input2__ = torch.randn(100, 128)
__input3__ = torch.randn(50, 100)
