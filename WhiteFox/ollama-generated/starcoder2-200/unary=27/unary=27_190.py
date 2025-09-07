
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, -0.75) # Setting the minimum value to -0.75
        v3  = torch.clamp_max(v2,  0.4)  # Setting the maximum value to 0.4
        return v3


# Initializing the model
m  = Model()
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

