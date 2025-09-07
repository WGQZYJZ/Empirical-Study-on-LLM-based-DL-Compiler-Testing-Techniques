
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) + 3
        v2  = F.relu6(v1) # ReLU6 is clamped at 6 for both upper and lower limit
        v3  = v2 * 4
        return v3 / 5

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
