
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
       return self.conv(x), F.sigmoid(self.conv(x))


# Initializing the model
m = Model()


# Inputs to the model (for each convolution layer)
x0 = torch.randn(256, 3, 480, 480)

# Convolution outputs
y1, y2 = m(x0)


