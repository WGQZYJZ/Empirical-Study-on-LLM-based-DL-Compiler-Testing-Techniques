
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(4, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = torch.clamp_min(v1, min=10.) # Clamp the output to a minimum value of `10.`
        v3  = torch.clamp_max(v2, max=95.) # Clamp the previous operation to a maximum value of `95`
        return v3

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(64)

