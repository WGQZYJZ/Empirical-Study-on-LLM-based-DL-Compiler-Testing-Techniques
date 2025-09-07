
class Model(torch.nn.Module):
    def __init__(self, maxval = 420738511, minval = -4292764771):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(in_channels=8, out_channels=3, kernel_size=(1, 1), stride=(1, 1))
 
    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = torch.clamp_min(v1, minval)
        v3 = torch.clamp_max(v2, maxval)

        return v3


m  = Model()

 # Inputs to the model
 x1  = torch.randn(1, 8, 64, 64)
 