
class Model(torch.nn.Module):
    def __init__(self, min=0., max=128.):
        super().__init__()
        self.linear = torch.nn.Linear(64*64*3, 7)
 
    def forward(self, x1):
        v1  = self.linear(x1.view(-1, 64*64*3))
        v2  = torch.clamp_min(v1, min)
        v3  = torch.clamp_max(v2, max) 
        return v3


# Initializing the model
m  = Model() 

 # Inputs to the model
x1 = torch.randn(64, 3*64*64)

 # Calling the model with inputs
