
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x1):
            v1 = self.conv(x1)
            v2 = v1 + 3 # Added here
            v3 = torch.clamp_min(v2,0) # Min value of the clamped result is set to 0
            v4 = torch.clamp_max(v3,6) 
            v5 = v4 / 6 # Divide by 6
        return v5
m = Model()


x1 = torch.randn(1,3,28,28)
__output__  = m(x1)
