
class Model(nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.negative_slope = negative_slope
    
    def forward(self, x1):
        v1 = torch.where(x1 > 0, x1, -self.negative_slope * (1 + torch.exp(-x1)))
        return v1


# Initializing the model
m = Model()
m = nn.LeakyReLU()
