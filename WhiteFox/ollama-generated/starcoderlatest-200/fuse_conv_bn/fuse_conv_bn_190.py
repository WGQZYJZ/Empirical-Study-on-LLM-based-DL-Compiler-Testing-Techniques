
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        y = torch.nn.functional.batch_norm(x, 1)
        return torch.nn.functional.conv2d(y, 1)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 32, 32)
