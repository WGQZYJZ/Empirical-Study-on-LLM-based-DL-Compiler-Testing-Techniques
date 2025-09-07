
class Model(torch.nn.Module):
    def __init__(self, minv=0., maxv=512.):
        super().__init__()

        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, kernel_size=(79, 1), stride=(240, 1))
        self.minv = minv
        self.maxv = maxv

    def forward(self, x):
      v1 = self.convtranspose(x)
      v2 = torch.clamp_min(v1, self.minv)
      v3 = torch.clamp_max(v2, self.maxv)

      return v3

# Initializing the model
m  = Model()

 # Inputs to the model