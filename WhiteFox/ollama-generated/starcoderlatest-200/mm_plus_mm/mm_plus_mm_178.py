
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2) # Matrix multiplication between x1 and x2
        v2 = torch.mm(x3, x4) # Matrix multiplication between x3 and x4
        v3 = v1 + v2  # Addition of the results of the two matrix multiplications
        return v3
 

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 3) # Input tensor 1
x2 = torch.randn(4, 5) # Input tensor 2
x3 = torch.randn(6, 7) # Input tensor 3
x4 = torch.randn(8, 9) # Input tensor 4


