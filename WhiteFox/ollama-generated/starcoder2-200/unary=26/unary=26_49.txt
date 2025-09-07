
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.deconv(x1)
        mask = v1 > 0
        slope = -0.5
        v2 = torch.where(mask, v1, slope * v1) # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v2

# Initializing model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

