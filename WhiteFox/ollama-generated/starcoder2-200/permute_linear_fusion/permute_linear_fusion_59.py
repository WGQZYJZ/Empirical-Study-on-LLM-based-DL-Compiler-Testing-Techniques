
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.nn.functional.linear(x1, 10)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(128)
