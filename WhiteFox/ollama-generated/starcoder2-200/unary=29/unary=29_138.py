
class Model(torch.nn.Module):
    def __init__(self, max_value=10):
        super().__init__()

        self.convtranspose  = torch.nn.ConvTranspose2d(32, 8, 3)
        self.clampmin   = nn.ClampMin(maxValue=15.)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
 
        v2  = v1.clamp_min(-7., max=70.)
        return v2


# Initializing the model
m  = Model()
 
 
