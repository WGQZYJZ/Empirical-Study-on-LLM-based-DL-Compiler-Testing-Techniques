
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 16, stride=16, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.tanh(v1)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(32, 8, 64, 64)
