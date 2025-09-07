
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 4, stride=2)
 
    def forward(self, x1, min_value=0., max_value=5.):
        return self.conv_transpose(x1, (min_value, max_value))

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
