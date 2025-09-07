
class Model(torch.nn.Module):
    def __init__(self, dim1=256):
        super().__init__()
        self.linear = torch.nn.Linear(dim1 + 784, dim1)

    def forward(self, x1, x2):

        v0 = torch.cat([x1, x2], 1)
        v1 = self.linear(v0)
        v2 = torch.tanh(v1)

        return v2


# Initializing the model
m = Model()

# Input to the model
x1 = torch.randn(37854, 9276)
