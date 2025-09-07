
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transposed = torch.nn.ConvTranspose2d(8, 3, 1, stride=2)
 
    def forward(self, x1):
        v1 = self.conv_transposed(x1)
        v2 = torch.tanh(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64*2, 64*2)
