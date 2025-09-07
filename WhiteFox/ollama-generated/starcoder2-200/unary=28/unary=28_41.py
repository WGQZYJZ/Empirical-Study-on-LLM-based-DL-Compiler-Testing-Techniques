
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 768)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, -3.593)
        v3 = torch.clamp_max(v2, 3.0)
        return v3

# Initializing the model
m = Model()

 # Inputs to the model