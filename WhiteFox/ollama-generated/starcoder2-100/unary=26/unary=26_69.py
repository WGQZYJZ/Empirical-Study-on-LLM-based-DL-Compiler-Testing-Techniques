
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose1d(8, 3, 4)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 > 0
        v3  = v1 * -v5[2]
        v4  = torch.where(v2, v1, v3)
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
x = torch.randn(8, 3, 90)
 
 