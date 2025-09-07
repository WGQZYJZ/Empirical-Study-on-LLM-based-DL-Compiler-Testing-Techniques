
class Model(torch.nn.Module):
    def __init__(self, minval=-0.5, maxval=1e-3):
        super().__init__()
        self.convtrans  = torch.nn.ConvTranspose2d(8, 4, kernel_size=(1, 1), padding=(0, 0))
 
    def forward(self, x1):
        v1  = self.convtrans(x1)
        v2  = torch.clamp_min(v1, minval= -0.5)
        v3  = torch.clamp_max(v2, maxval=  1e-3)
        return v3

# Initializing the model with default settings and fixed seed
m  = Model()
seed  = 42
torch.manual_seed(seed);

 # Inputs to the model