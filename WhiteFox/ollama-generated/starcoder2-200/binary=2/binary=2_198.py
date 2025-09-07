
class Model2(torch.nn.Module):
    def __init__(self, c=0):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v456 = v1 - c
        return v456


# Initializing the model
m2  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m2(x1)

