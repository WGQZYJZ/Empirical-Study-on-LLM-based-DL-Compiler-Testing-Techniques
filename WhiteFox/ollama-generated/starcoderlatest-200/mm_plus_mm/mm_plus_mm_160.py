
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1 = torch.nn.Linear(5, 4)
        self.mm2 = torch.nn.Linear(6, 7)
 
    def forward(self, x1, x2, x3):
        v1 = torch.mm(x1, x2) # Matrix multiplication between input1 and input2
        v2 = torch.mm(x3, x4) # Matrix multiplication between input3 and input4
        v3 = v1 + v2  # Addition of the results of the two matrix multiplications
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 3)
x2 = torch.randn(6, 4)
x3 = torch.randn(7, 9)
