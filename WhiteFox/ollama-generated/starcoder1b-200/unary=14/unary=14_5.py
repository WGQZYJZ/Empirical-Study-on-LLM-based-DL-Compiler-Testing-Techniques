
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 4, stride=1, padding=0)
 
    def forward(self, x):
        v = self.conv_transpose(x)
        return sigmoid(v)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
