
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, -10) # Clamp the minimum value for the clamping operation to be -10
        v3  = torch.clamp_max(v2, 4.578937867386925)# Clamp the maximum value of the previous operation to 4.578937867386925
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

