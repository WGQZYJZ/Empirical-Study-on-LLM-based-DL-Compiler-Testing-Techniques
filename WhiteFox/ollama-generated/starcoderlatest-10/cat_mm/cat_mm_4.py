
class Model(torch.nn.Module):
    def __init__(self, d):
        super().__init__()
        self.d = d
 
    def forward(self, x1):
        v1 = torch.mm(x1, x1)  # Apply matrix multiplication to the input tensor
        v2 = torch.cat([v1] * self.d, dim=0)  # Concatenate the output of matrix multiplication along dimension `0` (i.e., apply concatenation at the first dimension). `self.d` is a constant specified by the user.
        return v2


# Initializing the model
m = Model(4)
 
# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
