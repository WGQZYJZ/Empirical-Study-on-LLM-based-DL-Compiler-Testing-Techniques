
class Model(torch.nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.conv = torch.nn.Conv2d(input_size, output_size, 1)

    def forward(self, x1):
        conv1 = self.conv(x1)
        return conv1


# Initializing the model
m = Model(2, 2)


# Inputs to the model
x1 = torch.randn(3, 4, 5, 6)
