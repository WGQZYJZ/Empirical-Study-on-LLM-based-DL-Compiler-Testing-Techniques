
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(4, 2)
    
    def forward(self, x1):
       v0  = self.linear(x1)
       v1  = torch.clamp_min(v0, min=5.)
       v2  = torch.clamp_max(v1, max=7.) 
       return v2

# Initializing the model with random weights for each layer and optimizable variables in the graph.
model = Model()
inputtensor = torch.rand(size=(300, 4))
model.forward(x)


