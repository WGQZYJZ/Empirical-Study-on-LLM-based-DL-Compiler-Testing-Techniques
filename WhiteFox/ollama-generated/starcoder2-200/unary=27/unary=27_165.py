
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.clamp_min(v1, min=0), torch.clamp_max(v1, max=4096)


# Initializing the model
m = Model()


# Inputs to the model