
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1.clamp_min(10e-4) 
        v3  = torch.clamp_max(v2, 9000) 
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(5, 3, 64, 64)
 
# Evaluating the model
out  = m(x1)

 