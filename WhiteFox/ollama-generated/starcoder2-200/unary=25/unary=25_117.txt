
class Model(torch.nn.Module):
    def __init__(self, neg_slope=0.5):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
        self.neg_slope  = -1 * neg_slope
 
    def forward(self, x):
        v1 = self.linear(x) 
        v2 = v1 > 0 
        v3 = v1 * self.neg_slope  
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model with a negative slope of -0.5
m = Model(-0.5)
 
 
 # Inputs to the model 
x  = torch.randn(1, 3)
__output__= m(x)
