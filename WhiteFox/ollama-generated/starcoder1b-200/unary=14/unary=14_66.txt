
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 4, stride=2, padding=1)
 
    def forward(self, x):
        return self.conv(x)


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(4, 3, 64, 64)
