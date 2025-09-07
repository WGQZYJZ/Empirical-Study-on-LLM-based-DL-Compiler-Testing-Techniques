
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=4, kernel_size=(2, 2))
        self.bn1   = torch.nn.BatchNorm2d(num_features=4)

    def forward(self, x):
        return self.conv1(x).squeeze()


# Initializing the model
m = Model()

# Inputs to the model
input_tensor  = torch.randn(1, 3, 8, 8)
__output__    = m(input_tensor)


