
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):  # The model should be different from the previous one.
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(800, 765) # random input for input1 and input2 matrices of size (800, 765) respectively.
x2 = torch.randn(765, 934)
 
