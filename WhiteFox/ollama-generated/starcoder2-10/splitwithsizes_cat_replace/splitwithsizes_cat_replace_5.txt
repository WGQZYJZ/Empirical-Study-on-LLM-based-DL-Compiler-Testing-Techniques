
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = torch.split(x1, [32], dim=2) # split the input tensor to several tensors along dimension 2 and return a tuple
        v1  = v0[len(v0)-2] * 0.5 # multiply each of them by 0.5 using broadcasting
        v2  = torch.cat([v0[i].permute(3, 0, 1) for i in range(4)], dim=0).clone() + 5  # permute and concatenate the tensors along dimension 0 to return a new tensor
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 64)

__output__  = m(x1)

