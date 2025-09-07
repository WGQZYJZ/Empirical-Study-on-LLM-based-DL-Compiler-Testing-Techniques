
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1) 
        v2 = torch.clamp_min(v1, min_value=-1e7) # clamp to a minimum value of -1e7
        v3 = torch.clamp_max(v2, max_value=50.0) # clamp to a maximum value of 50.0 
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
 
# Generating valid initial inputs for the new model with clamp_min and clamp_max set
validInput = torch.clamp(torch.rand(size=(1, 3, 257, 257)) * -9000000 + 1e-4, min=(-1) * 5000, max=5000)
 
