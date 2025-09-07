
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        c = torch.nn.functional.conv2d(...)
        b = torch.nn.functional.batch_norm(...)
        return c + b


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
