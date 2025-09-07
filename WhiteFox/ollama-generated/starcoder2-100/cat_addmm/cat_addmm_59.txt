
class Model(torch.nn.Module):
    def __init__(self, dim=32):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(in_channels=10, out_channels=64, kernel_size=5)
 
    def forward(self, x):  # Assume the input is already 8x8 pixels
        conv1 = self.conv(x)
        return conv1.reshape(-1, dim)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.rand(2560, 10, 8, 8).requires_grad_()

