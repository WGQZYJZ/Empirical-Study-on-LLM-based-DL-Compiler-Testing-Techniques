
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.relu(x1)  # Apply relu to x1
        v2 = torch.tanh(x2)  # Apply tanh to x2
        return v1 + v2


# Inputs to the model
v1 = torch.randn(...)
v2 = torch.randn(...)
