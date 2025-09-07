
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(3, 16, 4, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3

 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 512, 512)
