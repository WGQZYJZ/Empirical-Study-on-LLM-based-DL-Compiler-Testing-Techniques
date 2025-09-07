
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0) # clamped result of adding constant "3" to conv output
        v4  = torch.clamp_max(v3, 6)# clamped result of clamping previous operation to minimum and maximum values [0, 6] 
        v5  = v1 * v4 # multiplied result of conv output by clamped operation above   
        v6  = v5 / 6 # divided result of multiplication
        return v6
 
# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
