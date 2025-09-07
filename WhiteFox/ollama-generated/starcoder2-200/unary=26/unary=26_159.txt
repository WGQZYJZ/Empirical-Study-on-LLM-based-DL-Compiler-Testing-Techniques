
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.relu  = torch.nn.ReLU()
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 > 0
        v3  = v1 * negative_slope 
        v4  = torch.where(v2, v1, v3)
        return v4

 # Initializing the model
negative_slope = 0.5
m = Model(negative_slope=negative_slope)

 # Inputs to the model 
 x = torch.randn(1, 8, 64, 64)

 # Output of the model
