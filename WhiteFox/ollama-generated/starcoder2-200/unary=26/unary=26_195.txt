
class Model(torch.nn.Module):
    def __init__(self, negative_slope = 0.5):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3,8,1)
        self.relu = nn.ReLU()
 
    def forward(self, x1):
        v1  = self.convT(x1) 
        v2 = (v1 > 0).type_as(v1)
        v4 = torch.where(v2, v1, -v3*v2)
        return v4

# Initializing the model with a negative slope
m  = Model(-0.5)

 # Inputs to the model
x1  = torch.randn(1, 3,64, 64)
 
 