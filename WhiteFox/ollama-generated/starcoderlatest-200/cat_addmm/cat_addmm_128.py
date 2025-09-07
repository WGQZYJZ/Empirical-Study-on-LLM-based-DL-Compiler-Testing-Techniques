
class Model(torch.nn.Module):
    def __init__(self, d):
        super().__init__()
        self.linear = torch.nn.Linear(3072, 1)
 
    def forward(self, x):
        v1 = torch.addmm(x, self.w, self.b)
        v2 = torch.cat([v1], dim=1)
        return v2
 
 # Initializing the model
m = Model(64)
 
# Inputs to the model
x1 = torch.randn(1, 3072)
