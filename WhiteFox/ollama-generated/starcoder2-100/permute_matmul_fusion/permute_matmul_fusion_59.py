
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A
        v2 = x2.permute(0, 2, 1) # Permute the input tensor B
        v3 = torch.bmm(v1, v2) 
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(45, 90, 87).permute((2, 0, 1)) # Input tensor A for m.forward(...)
x2 = torch.randn(33, 65, 78) # Input tensor B for m.forward(...)
__output__  = m(x1, x2)
