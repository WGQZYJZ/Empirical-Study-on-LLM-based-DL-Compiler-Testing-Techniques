
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(24*51, 3)
 
    def forward(self, x1):
       v1 = self.linear(x1)
       v2 = torch.clamp_min(v1, -0.9857617950439453)
       v3 = torch.clamp_max(v2, 1.0214531421661377)

# Initializing the model