
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, **kargs):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, kargs['min'])
        v3 = torch.clamp_max(v2, kargs['max'])
        return v3


# Initializing the model and providing arguments for the minimum value and maximum value
m = Model()
m._set_state_dict({'conv_transpose': {'weight': torch.randn(10, 8, 64, 64)}})
x1 = torch.randn(1, 3, 64, 64)
v3 = m(x1, min=kargs['min'], max=kargs['max'])


