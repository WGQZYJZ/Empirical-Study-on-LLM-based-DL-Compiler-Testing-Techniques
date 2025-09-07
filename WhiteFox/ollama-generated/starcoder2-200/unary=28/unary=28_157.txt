
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(128, 3)
 
    def forward(self, x1):
        v0  = self.linear(x1)
        return torch.clamp_min(v0, min(-5))

m  = Model()

 # Inputs to the model