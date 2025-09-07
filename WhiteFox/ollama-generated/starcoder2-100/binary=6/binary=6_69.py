
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
       v1 = self.linear(x1) - other
       return v1

# Initializing the model
m  = Model()

 # Inputs to the model
other = torch.randn(64)
x1 = torch.randn(1, 327680)
__output__  = m(x1)
