
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.sigmoid(v1) # apply sigmoid function
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x = torch.randn(1, 3, 64, 64)
__output__  = m(x)