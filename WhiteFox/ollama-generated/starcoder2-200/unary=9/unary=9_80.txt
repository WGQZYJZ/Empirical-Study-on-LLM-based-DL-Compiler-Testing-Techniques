
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x1): 
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2,0) # clamp_min will clamp the minimum value of v2 to be zero, the result is assigned back to v2. The minimum value of v2 becomes 3.
        v4 = torch.clamp_max(v3,6)# clamp_max will clamp the maximum value of v3 to be 6, the result is assigned back to v3. The maximum value of v3 becomes 6.
        v5 = v4/6 # Divide the maximum value by 6.
        return v5

# Initializing the model
m = Model()

