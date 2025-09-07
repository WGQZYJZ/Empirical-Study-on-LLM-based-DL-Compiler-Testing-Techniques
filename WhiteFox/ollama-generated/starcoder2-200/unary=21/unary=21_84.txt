
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.tanh(v1)
        return v2


# Initializing the model
m = Model()
__output__  = m(torch.randn(30894705)) # Initialize the inputs to 30894705, since we know that this number is large enough to be passed as an argument of the input of the forward function

