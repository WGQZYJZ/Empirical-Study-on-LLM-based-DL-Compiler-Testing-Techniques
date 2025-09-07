
class Model2(torch.nn.Module):
    def __init__(self, ):
        super().__init__()
        self.l1 = torch.nn.Linear()
 
    def forward(self, x):
        v  = self.l1(x)
        v = v * 0.5
        return v


# Initializing the model
m2 = Model2()
# Inputs to the model
x3 = torch.randn(48, 768)
__output___2__ = m2(x3)
 
