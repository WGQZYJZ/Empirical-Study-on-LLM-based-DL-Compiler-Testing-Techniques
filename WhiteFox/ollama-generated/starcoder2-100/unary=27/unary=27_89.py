
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, -0.5, max_value=32768) # Clamp the output of the convolution to a maximum value
        v3  = torch.clamp_max(v2, -128, max_value=128)   # Clamp the output of the previous operation to a maximum value
        return v3


# Initializing the model
m  = Model()
__output__  = m(x1)

## End of text
