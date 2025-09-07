
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=0.9768847)
        v3 = torch.clamp_max(v2, max=0.5920044851303101)
        return v3


# Initializing the model and inputs to it