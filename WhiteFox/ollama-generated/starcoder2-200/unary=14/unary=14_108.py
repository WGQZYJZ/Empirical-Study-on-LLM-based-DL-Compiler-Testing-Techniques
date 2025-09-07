
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = nn.functional.sigmoid(v1) # Here the sigmoid function is imported from torch.nn.functional (imported as nn.functional), which makes the code more readable and maintainable.
        v3  = v1 * v2
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 8, 56, 56)
__output__  = m(x1)

