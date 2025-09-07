

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2   = torch.clamp_min(v1, min=0.5) # Clamp the output of the convolution to a minimum value (0.5 in this case).
        v3  = torch.clamp_max(v2, max=768) # Clamp the result of the previous operation to a maximum value (768 in this case).
        return v1

# Initializing the model
m  = Model()
x1   = torch.randn(3, 3, 950, 950)

