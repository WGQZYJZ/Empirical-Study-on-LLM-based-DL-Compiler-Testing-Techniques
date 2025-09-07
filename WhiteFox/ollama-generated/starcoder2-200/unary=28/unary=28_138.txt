
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear()
 
    def forward(self, x1):
        v1 = linear(x1)
        v2 = torch.clamp_min(v1, min_value=0.)
        v3 = torch.clamp_max(v2, max_value=50.)
        return v3

# Initializing the model with the minimum and maximum values provided as keyword arguments
m  = Model()

 # Inputs to the model for this example
x1 = torch.randn(1, 4)

 __output__  = m(x1)
 

