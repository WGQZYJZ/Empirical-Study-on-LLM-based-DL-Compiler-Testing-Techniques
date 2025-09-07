
class Model(torch.nn.Module):
    def __init__(self, min_value=-0.5, max_value=2.1439786) :
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1, min=-0.5) # Clamps the value in v1 to -0.5
        v3  = torch.clamp_max(v2, max=2.1439786)
        return v3


# Initializing model and setting seeds for reproducible results:
m  = Model()
random.seed(0)
torch.manual_seed(0)
 
# Creating input data using torch.rand():
x  = torch.rand((1, 3, 256, 49))
 
 # Obtaining output of the model: 
 __output__  = m(x)

