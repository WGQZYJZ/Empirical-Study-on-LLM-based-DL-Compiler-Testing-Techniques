
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(1, 3)
        self.m2 = torch.nn.Linear(50, 70)
 
    def forward(self, x1):
        v1 = torch.mm(x1, self.m1.weight) + self.m1.bias # Matrix multiplication between the input and matrix with weights (including bias)
        v2 = torch.mm(v1, self.m2.weight) + self.m2.bias # Matrix multiplication between the output of first multiplication and matrix with weights (including bias)
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
