
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.relu(v1) 
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(48000, 3, 64, 90)
__output__  = m(x1)

- - -
- - -
