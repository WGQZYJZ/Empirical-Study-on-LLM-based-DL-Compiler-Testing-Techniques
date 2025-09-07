
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp(v1 + 3, min=0, max=6) # clamped by default between 0 and 6
        v3 = v2 / 6 # divided by 6
        return v3

# Initializing the model