
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.conv  = torch.nn.Conv2d(16, 32, kernel_size=(7))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).to(torch.float) 
        v3 = v1 * (-negative_slope)  
        v4 = torch.where(v2 ,v1, v3 ) 
        return v4

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(8, 16, 50, 50)

# Outputs of the model with the initial negative_slope argument set to -negative_slope=0.3
