
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = x1.permute(0, 2, 3, 1)
        return torch.mean(v1, dim=4).view(x1.shape[0], x1.shape[2], -1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 2, 4)
