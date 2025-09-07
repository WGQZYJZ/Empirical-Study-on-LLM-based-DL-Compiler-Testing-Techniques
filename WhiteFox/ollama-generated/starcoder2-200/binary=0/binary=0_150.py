
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + t1
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
t1  = torch.randn(50, 8, 64, 64)
__output__  = m(x1, t1=t1)

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
t1 = torch.randn(50, 8, 64, 64)
 
# Outputs from the model
__output1__, __output2__ = m(x1), m(t1=t1)

