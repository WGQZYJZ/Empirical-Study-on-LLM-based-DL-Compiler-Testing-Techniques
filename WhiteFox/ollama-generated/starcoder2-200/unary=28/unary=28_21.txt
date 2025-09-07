
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1, 2)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = torch.clamp_min(v1, -0.4596738821272523) # Minimum value: -0.4596738821272523
        v3  = torch.clamp_max(v2, 0.992451487137557) # Maximum value: 0.992451487137557
 
        return v3

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.tensor([-0.67, -0.32], requires_grad=True)

