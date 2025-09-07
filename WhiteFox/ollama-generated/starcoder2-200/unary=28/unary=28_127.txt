
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=0.)
        return torch.clamp_max(v2, max=15.).float()

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(32)
 __output__  = m(x1)
 
 
