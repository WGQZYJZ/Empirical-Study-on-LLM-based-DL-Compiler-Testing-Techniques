
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.norm1 = torch.nn.LayerNorm((64, 64), elementwise_affine=False)
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.norm1(x)
        v2 = self.conv1(v1)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
q  = torch.randn(1, 3, 64, 64)
k  = torch.randn(8, 3, 64, 64)
v  = torch.randn(8, 3, 64, 64)
