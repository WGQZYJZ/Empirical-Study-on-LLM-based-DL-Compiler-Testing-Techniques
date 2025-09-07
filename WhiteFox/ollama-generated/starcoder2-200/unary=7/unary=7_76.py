
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1024)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = torch.clamp(v1, min=0, max=6)
        v3  = v1 + 3
        v4  = torch.clamp(v3, min=0, max=6)
        v5  = v2 / 6.0
        return v5


# Initializing the model
m2  = Model()

 # Inputs to the model