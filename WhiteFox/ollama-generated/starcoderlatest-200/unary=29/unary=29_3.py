
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 3, 4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min_value=0.)
        v3 = torch.clamp_max(v2, max_value=1.)
        return v3

# Initializing the model and providing minimum and maximum values as keyword arguments
m = Model()
m = m.eval().cuda().float() # eval() disables dropout
