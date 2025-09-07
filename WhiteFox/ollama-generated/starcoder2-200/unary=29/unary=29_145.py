
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=128.)
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(32, 64, kernelSize=(5, 5))
 
    def forward(self, x):
        v1  = self.convT(x)
        v2  = torch.clamp_min(v1, minValue=min_value)
        v3  = torch.clamp_max(v2, maxValue=max_value)
        return v3

 # Initializing the model
 m = Model()
 
 # Inputs to the model
 x  = torch.randn(4, 64, 100, 100)
 __output__  = m(x)


