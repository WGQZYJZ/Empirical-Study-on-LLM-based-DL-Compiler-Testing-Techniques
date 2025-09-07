
class Model(torch.nn.Module):
    def __init__(self, min_value=-1, max_value=50):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1)
    
    def forward(self, x1):
        v1 = self.deconv(x1)
        v2 = torch.clamp_min(v1, min=min_value) 
        v3 = torch.clamp_max(v2, max=max_value)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)

# Outputs from the model
y1 = m(x1)

## This model will be submitted as a .txt file, please name it "model.txt".

