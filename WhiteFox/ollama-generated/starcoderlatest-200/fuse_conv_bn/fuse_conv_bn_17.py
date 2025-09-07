
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, (3, 3))

    def forward(self, x):
        output = torch.nn.functional.batch_norm(self.conv(x), None)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 2, 3, 4)
