
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = x1.permute(...) # Permute the input tensor
        t2 = torch.nn.functional.linear(t1, ...) # Apply linear transformation to the permuted tensor.
        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
