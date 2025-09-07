
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + t0.randn((v1.size(-2), v1.size(-1))).to(torch._C._cuda_current_device())
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1,3,64,64)


