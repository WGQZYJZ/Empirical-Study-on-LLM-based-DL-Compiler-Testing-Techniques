
class Model(torch.nn.Module):
    def __init__(self,  min_value=0., max_value=10.):
        super().__init__()
        self.linear = torch.nn.Linear()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, 10.)
        return torch.clamp_max(v2, max_value=5.)


# Initializing the model with fixed keyword arguments
m = Model()

 # Inputs to the model
x1 = torch.randn(3, 64)
