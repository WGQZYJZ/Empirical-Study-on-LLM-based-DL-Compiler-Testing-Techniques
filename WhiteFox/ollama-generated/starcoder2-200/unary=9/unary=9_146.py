
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 
        v3  = torch.clamp_min(v2,0 ) # Clamp the result to a minimum of `0`
        v4  = torch.clamp_max(v3,6) # Clamp the previous output to a maximum of `6`
        v5  = v4 / 6 # Divide the previous output by 6
        return v5

# Initializing the model
m = Model()


