
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1, stride=1, padding=0)

    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0) # Clamp the result of addition to a minimum value of 0
        v4  = torch.clamp_max(v3, 6) # Clamp the previous result to maximum value of 6
        v5  = v4 / 6 
        return v5


# Initializing and running the model
m = Model()
__output__  = m(x1)