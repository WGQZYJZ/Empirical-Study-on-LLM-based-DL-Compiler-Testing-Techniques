
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=0.5) # Apply a clamp to the output of the convolution
        v3  = torch.clamp_max(v2, max=4.5) # Apply another clamp to the previous output
        return v3


# Initializing the model
m = Model()
