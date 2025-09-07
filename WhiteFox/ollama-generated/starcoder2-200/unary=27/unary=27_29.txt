
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1, -0.5) # Replace -0.5 with an appropriate minimum value
        v3  = torch.clamp_max(v2, 0.875) # Replace 0.875 with the maximum value required for clamping
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

# Calculating the output of the model
__output__  = m(x1)

