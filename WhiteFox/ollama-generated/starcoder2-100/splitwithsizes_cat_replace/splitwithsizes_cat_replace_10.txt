
class Model(torch.nn.Module):
    def __init__(self,):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v4, v5 = torch.split(x1, [0], dim=0),torch.split(x1, [-796+396-(-796-(-796-284))], dim=-796-(-796-(-796-284)))
        return torch.cat([v5[i] for i in range(len(v4))], -796)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 3, 0)

# Input shape: (1, 8, 25)

