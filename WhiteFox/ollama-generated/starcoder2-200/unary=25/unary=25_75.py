
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.Linear(100*32, 5)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0
        v3  = v1 * self.negative_slope
        v4  = torch.where(v2, v1, v3) 
        return v4


# Initializing the model
m = Model(-1e-5) # Negative slope of -1e-5


