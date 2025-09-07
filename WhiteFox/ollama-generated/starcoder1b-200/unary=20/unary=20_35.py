
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
        self.tanh  = torch.nn.Tanh()
 
    def forward(self, x):
        v1 = self.conv(x)
        return self.tanh(v1)


# Initializing the model
m = Model()


# Inputs to the model
__input__ = ...
__output__  = m(__input__)


