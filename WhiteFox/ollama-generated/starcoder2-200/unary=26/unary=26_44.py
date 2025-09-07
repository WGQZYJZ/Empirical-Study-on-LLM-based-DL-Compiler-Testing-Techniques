
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
        self.relu  = nn.ReLU()
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1   = self.conv(x1) 
        v2   = (v1 > 0).float() * self.negative_slope + v1.abs() * (v1 < 0)
        return self.relu(v2)


# Initializing the model
m  = Model(negative_slope=0.5) # Passing the negative slope of 0.5 to __init__
