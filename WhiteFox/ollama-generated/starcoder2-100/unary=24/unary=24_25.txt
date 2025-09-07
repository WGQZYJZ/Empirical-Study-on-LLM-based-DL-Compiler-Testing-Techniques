
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = v1 * (-self.negative_slope if -self.negative_slope < 0 else 0) 
        v4 = torch.where(v2, v1, v3) # Replace with v3 once PyTorch implements the where function
        return v4

# Initializing the model and setting the negative slope to 0.2
m = Model(negative_slope=0.2)


# Inputs to the model