
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l = torch.nn.Linear(30, 18)
 
    def forward(self, x1):
        v1 = self.l(x1)
        v2 = v1 * (v1 + 3).clamp(min=0, max=6) / 6
        return v2

# Initializing the model and its input tensor:
m  = Model()

