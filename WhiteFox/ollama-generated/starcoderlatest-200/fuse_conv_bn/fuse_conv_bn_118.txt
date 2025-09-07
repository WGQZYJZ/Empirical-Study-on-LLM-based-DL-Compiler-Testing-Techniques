
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 3, kernel_size=3)

    def forward(self, x):
        v1 = F.relu(self.conv1(x)) # the output is tracked in BN statistics and BN momentum accumulator
        return v1


# Inputs to the model
x = torch.randn(1, 2, 4, 4)
