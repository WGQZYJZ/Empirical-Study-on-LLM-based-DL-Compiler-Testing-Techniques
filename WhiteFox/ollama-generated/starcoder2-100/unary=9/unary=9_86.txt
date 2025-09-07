
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0)
        v4  = torch.clamp_max(v3, 6)
        v5  = v4 / 6 # clamped_output / 6
        return v5


m  = Model()
 
 

x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

# Inputs to the model
x1  = torch.randn(2, 3, 80, 80) # input tensor with shape of 3D and size of (N=2, C=3, H=80, W=80). This value should be different from x1 in the previous model
__output__  = m(x1)

