
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input1 = torch.nn.Parameter(torch.randn(2, 3)) 
        self.input2 = torch.nn.Parameter(torch.randn(3, 4))
        self.conv = torch.nn.Conv2d(5, 6, 1, stride=1, padding=0)

    def forward(self, x):
        v1 = torch.mm(x, self.input1) # Matrix multiplication between input1 and input3
        v2 = torch.mm(x, self.input2) # Matrix multiplication between input1 and input3
        v3 = v1 + v2  # Addition of the results of the two matrix multiplications
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 5, 64, 64)
