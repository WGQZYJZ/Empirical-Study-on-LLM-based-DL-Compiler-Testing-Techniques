
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(3, 8, kernel_size=16, stride=4)
 
    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = torch.nn.functional.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
