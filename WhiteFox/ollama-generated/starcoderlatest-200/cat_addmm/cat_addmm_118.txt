
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x1, x1) # Apply matrix multiplication with a batch norm applied to the result of adding two input tensors
        v2 = torch.cat([v1], dim=0)  # Concatenate along dimension 0
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(2, 3, 32, 32)
