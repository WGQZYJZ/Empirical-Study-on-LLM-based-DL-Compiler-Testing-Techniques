
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Forward function should be written as following
        return torch.relu(x1)  # Pointwise unary operation


# Initializing the model
m = Model()


