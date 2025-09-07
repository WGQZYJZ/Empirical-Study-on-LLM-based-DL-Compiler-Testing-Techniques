
class Model(torch.nn.Module):
    def __init__(self, maxv=10., minv=-2.568437988044784):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x):
        v1 = self.convt(x)
        v2 = torch.clamp_min(v1, minv)
        v3 = torch.clamp_max(v2, maxv)

        return v3


# Initializing the model
m  = Model()
