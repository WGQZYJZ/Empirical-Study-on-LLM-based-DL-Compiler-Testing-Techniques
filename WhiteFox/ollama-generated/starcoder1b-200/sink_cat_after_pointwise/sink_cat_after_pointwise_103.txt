
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.relu(x1)  # ReLU of x1
        v2 = torch.tanh(x2)  # Tanh of x2
        return torch.cat([v1, v2], dim=1)


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 3)
x2 = torch.randn(1, 3, 3)
