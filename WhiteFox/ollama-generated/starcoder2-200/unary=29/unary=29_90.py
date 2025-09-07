

class Model(torch.nn.Module):
    def __init__(self, min_, max_):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1)
        self.min  = min_ # Clamp to a minimum value in this range
        self.max  = max_ # Clamp to a maximum value in this range
 
    def forward(self, x):
        v1  = self.conv_transpose(x) 
        v2  = torch.clamp(v1, self.min, self.max)
        return v2

# Initializing the model