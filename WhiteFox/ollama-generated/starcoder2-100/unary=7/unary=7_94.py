
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(6, 24)
 
    def forward(self, x1):
        v1 = self.l1(x1)
        v2 = clamped_output  = v1 + 3
        v3 = torch.clamp(min=0, max=6, input_=v2) 
        v4 = v1 * v3
        v5 = v4 / 6
        return v5


# Initializing the model