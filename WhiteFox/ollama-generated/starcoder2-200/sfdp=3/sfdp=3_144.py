
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.matmul(x1[:, None], 0 * self)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(256, 784)

# Output of the model
m(x1).shape

(256, 3, 256, 256)