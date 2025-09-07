
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(320, 640, kernel_size=1)
 
    def forward(self, x):
        v1   = self.conv(x)
        v2t  = torch.ones(v1.shape).cuda() 
        v2   = (v1 > v2t).float()*negative_slope
        return v1*v2

# Initializing the model
model = Model(0.4)

 # Inputs to the model
input = torch.randn(3, 50, 70, 80)
__output__   = model(input)

