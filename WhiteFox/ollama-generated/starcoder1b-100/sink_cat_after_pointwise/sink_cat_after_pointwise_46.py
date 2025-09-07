
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x2 = x1.view(-1, 2).permute(0, 1)
        return torch.relu(x2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4)
