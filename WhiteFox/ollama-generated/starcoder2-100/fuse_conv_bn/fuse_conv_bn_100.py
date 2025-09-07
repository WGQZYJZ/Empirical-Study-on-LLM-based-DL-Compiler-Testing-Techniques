
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 80, 5)

    def forward(self, x):
        output = torch.nn.functional.conv2d(x, self.conv1.weight, self.conv1.bias)
        return torch.nn.functional.batch_norm(output)


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(4, 3, 28, 28)
__output__  = m(x)

