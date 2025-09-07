
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0)
        v4  = torch.clamp_max(v3, 6)
        return (v4 / 6).sum()


# Initializing the model and input tensor
m  = Model()
x1  = torch.randn(1, 8, 32, 32)


# Initializing the model without reusing the previous input variable x1
m  = Model()
 