
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = torch.clamp_min(v1, min_value) 
        return torch.clamp_max(v2, max_value)


# Initializing the model
m  = Model() 

# Inputs to the model
__output__  = m(torch.randn(300, 8, 64, 64))

