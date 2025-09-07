
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scale_factor = 0.7071067811865476
        self.bias = None
 
    def forward(self, x):
        v  = self.conv(x) / self.scale_factor
        b  = torch.zeros(1).to(x.device)
        c  = torch.cat([v, b], dim=-1)
        return torch.tanh(c)


# Initializing the model
m = Model()


