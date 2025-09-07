
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        v2 = v1.permute() # NOTE: the permute is missing from this line (the model becomes different).
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3, 5)
