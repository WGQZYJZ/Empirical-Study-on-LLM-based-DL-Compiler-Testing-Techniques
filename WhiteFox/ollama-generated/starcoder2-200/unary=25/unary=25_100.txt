
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(20, 5)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0 
        v3  = -v1 * negative_slope
        v4  = torch.where(v2, v1, v3 )
        return v4

# Initializing the model
m  = Model()
m.conv.weight[:] = nn.Parameter(torch.ones([5, 20]) * 0) # Initialize the weight of the first linear layer as [0] * 5 and [1] * 20
negative_slope  = -3.7

# Inputs to the model
x1  = torch.randn(1, 20)
__output__  = m(x1)

# Output comparison (Optional)

