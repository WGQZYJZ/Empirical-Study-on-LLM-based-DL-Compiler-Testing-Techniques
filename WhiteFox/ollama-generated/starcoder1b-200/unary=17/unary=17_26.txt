
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
output_tensor = m(input_tensor)
