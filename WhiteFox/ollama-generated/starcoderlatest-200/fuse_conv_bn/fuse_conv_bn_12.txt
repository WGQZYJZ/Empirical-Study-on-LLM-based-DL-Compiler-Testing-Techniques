
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=(1, 3))
        self.batch_norm = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        return F.relu(self.conv1(x) + self.batch_norm(x))

# Inputs to the model
x = torch.randn(1, 3, 10, 4)
