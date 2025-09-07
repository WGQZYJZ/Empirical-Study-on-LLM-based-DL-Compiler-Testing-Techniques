
class Model(torch.nn.Module):
    def __init__(self, conv_weight=32):
        super().__init__()

        self.conv = torch.nn.Conv1d(16, 30, kernel_size=(15), stride=(4))
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        x = x * (np.random.rand() + 1)

        output = self.conv(x)
        output += self.bn(output)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 480)
__output__  = m(x)