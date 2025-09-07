
class Model(torch.nn.Module):
    def __init__(self, min_value: float = 0, max_value: float = 1):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=0.5)
        v3 = torch.clamp_max(v2, max=0.7071067811865476)
        return v3


# Initializing the model and setting the minimum and maximum values
m = Model()
min_value: float = 0.5 # Minimum value clamped to
max_value: float = 0.7071067811865476 # Maximum value clamped to
