
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()


# Inputs to the model
input1 = torch.randn(8, 5) # Shape [10]
input2 = torch.randn(10, 4) # Shape [10]
input3 = torch.randn(8, 6) # Shape [10]
input4 = torch.randn(10, 7) # Shape [10]
