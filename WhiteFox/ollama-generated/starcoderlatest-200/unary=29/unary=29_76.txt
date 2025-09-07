
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 32, 4, stride=4)
 
    def forward(self, x1, **args):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min_value=0.5)
        v3 = torch.clamp_max(v2, max_value=0.7071067811865476)
        return v3
# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
