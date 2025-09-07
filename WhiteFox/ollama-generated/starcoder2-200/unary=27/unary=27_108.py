
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1.clamp_min(-0.5) # Clamp the output of the convolution to a minimum value -0.5
        v3  = v2.clamp_max(200.)  # Clamp the output of the previous operation to a maximum value 200.
        return v3

# Initializing the model
m = Model()
__output__  = m(x1)

