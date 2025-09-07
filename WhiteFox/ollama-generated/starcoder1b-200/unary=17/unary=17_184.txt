
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(8, 3, 4, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv_t(x)
        return relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
