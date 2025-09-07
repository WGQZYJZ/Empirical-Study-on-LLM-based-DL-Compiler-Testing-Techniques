
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v2 = torch.clamp_min(x1, -0.5)
        v4 = torch.clamp_max(v2, +0.769)
        return v4


# Initializing the model
m = Model()

 # Inputs to the model 
x1 = torch.randn(1, 3, 8, 8)

 