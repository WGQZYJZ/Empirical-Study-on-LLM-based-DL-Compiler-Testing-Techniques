
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min_value=0)
        v3 = torch.clamp_max(v2, max_value=0.5)
        return v3


# Initializing the model and providing keyword arguments for clamping values
m = Model()
m = m.to(torch.device('cuda'))
min_value  = -1.0
max_value =  1.0


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64).to(torch.device('cuda'))
