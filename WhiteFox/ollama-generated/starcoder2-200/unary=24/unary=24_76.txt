
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.159):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0 
        v3  = v1 * negative_slope
        v4  = torch.where(v2, v1, v3)
        return v4

 # Initializing the model
 m = Model()
 
 # Inputs to the model
 x1  = torch.randn(1, 3, 64, 64)
 
# Generating the input tensor for the model
x2  = torch.empty(x1.size()).uniform_(0, -negative_slope + 1).detach().requires_grad_()
 
 # Initializing a new model with a different architecture than that of m 
 m1 = Model(negative_slope=0.89)
 
# Initializing a new model with a different architecture from the previous one 
m2  = Model(negative_slope=7.56434e-4)

