
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, -96.) # Set the minimum value to a negative number and try to clamp it between -96.0 and +96.0.
        v3  = torch.clamp_max(v2, 96.) # Try to set the maximum value as -97.
        return v3


# Initializing the model
m = Model()


# Inputs to the model