
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 8, kernel_size=3)
 
    def forward(self, x1, x2, x3):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8096, 16) # input1
x2 = torch.randn(8096, 16) # input2
x3 = torch.randn(8096, 16) # input3
