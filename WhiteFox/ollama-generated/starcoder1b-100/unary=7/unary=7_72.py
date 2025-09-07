
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8)
        self.clamp   = clamp  # Using clamped function as the input/output of `linear`
 
    def forward(self, x):
        l = self.linear(x)
        return clamp(min=0, max=6, l + 3) / 6


# Initializing the model
m = Model()

