
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.permute(x1, 0) # Permute the input tensor
        v2  = torch.nn.functional.linear(v1, 99) 
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(4)
__output__  = m(x1)

