
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.clamp_min(v1, -0.5),\
               torch.clamp_max(v1 * v2 + 3, 7.4),\
               torch.clamp_max(-6.73 / v3, -89.01),\
               torch.clamp_max(torch.div(500.34 * v4 + x, v2), v5),\
               torch.clamp_min(v1 + 74, 5.0)


# Initializing the model
m = Model()

# Inputs to the model