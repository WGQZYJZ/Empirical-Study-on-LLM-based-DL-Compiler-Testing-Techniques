
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # ...
        return torch.cat([x2])

# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
