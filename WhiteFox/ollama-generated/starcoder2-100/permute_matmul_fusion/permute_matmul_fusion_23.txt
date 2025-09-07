
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.nn.functional.linear(x1.permute(-3, -2), 8) # Permute the input tensor A first then apply linear transformation on it.
        v2 = torch.bmm(v1, x2) # Apply bmm on both tensors after permuting them.
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(16, 4, 3)
x2  = torch.randn(8, 3, 5)
__output__  = m(x1, x2)