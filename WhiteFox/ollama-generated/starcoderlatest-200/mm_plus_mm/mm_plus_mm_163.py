
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input1 = torch.randn(2, 8, 64, 64)
        self.input2 = torch.randn(3, 10, 16, 16)
 
    def forward(self, x1):
        v1 = torch.mm(x1, x1) # Matrix multiplication between input1 and input1
        v2 = torch.mm(x1, x2) # Matrix multiplication between input1 and input2
        v3 = v1 + v2 # Addition of the results of the two matrix multiplications
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 64, 64)
x2 = torch.randn(2, 2, 16, 16)
