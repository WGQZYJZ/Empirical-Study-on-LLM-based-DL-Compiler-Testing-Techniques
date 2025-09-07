
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1)
 
    def forward(self, x1):
        v0  = self.conv(x1)
        v1  = v0 - torch.randn_like(v0).float()
        v2  = v1[torch.ge(v1, 0)]
        return v2

# Initializing the model
m = Model()


# Inputs to the model