
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Input shape: Nx4x4x3
        conv = torch.nn.Conv2d(in_channels=3, out_channels=8, kernel_size=(3, 3), stride=(1,), padding=(0,))
        bn = torch.nn.BatchNorm2d(num_features=8)

        v  = conv(x1) # Shape: Nx4x4x8
        v  = bn(v) # Shape: Nx4x4x8
        v  = torch.nn.functional.relu(v, inplace=True) # Shape: Nx4x4x8

        return v

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 4, 4)

