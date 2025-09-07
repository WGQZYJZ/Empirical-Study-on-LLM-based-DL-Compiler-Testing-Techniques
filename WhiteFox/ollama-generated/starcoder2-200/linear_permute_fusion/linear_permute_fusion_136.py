
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        v2  = v1.permute(0, 3, 2, 4) # permute the last two dimensions of the output tensor with more than 2 dimensions.
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(5, 8, 6, 30)
__output__  = m(x1)

