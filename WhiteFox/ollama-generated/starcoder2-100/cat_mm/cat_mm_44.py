
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = t1 + t1 + ... + t1 # This model will be different from the previous one
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1, x2 = torch.randn(3072), torch.randn(4, 5)
__output__  = m([x1, x2])