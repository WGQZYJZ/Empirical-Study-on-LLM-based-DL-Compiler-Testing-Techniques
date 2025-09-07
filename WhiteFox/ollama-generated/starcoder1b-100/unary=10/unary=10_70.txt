
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1).clamp_min(0)
        return v1 / 6


# Initializing the model
m = Model()


