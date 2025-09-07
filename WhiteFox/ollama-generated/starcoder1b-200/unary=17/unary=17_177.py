
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv_transpose(x)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(4, 8, 64, 64)
