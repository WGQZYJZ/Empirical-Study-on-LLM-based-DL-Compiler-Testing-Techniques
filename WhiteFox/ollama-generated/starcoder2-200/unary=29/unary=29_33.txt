
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.clamp_min(v1, min=-0.45) # Min value -0.45 
        v3  = torch.clamp_max(v2, max=976.0) # Max value 976.0
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 485, 7520).to(device=torch.device("cpu")) # min value -0.45, max_value  976.0
__output__  = m(x1)

