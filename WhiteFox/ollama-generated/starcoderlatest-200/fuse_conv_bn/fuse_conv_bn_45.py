
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = torch.nn.functional.conv2d(x, 10)
        x = torch.nn.functional.batch_norm(x)
        return x


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 16, 8, 8)
