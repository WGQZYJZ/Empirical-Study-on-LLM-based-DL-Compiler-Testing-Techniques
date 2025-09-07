
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1.0):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.sigmoid = nn.Sigmoid()
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, v1, self.negative_slope * v1) # t1 > 0 => select elements from v1 and multiply by the negative slope
        v3 = v2 * x1 # multiplies v2 with each element in x1
        v4 = torch.erf(v3)
        return v4

# Initializing the model
m = Model()

