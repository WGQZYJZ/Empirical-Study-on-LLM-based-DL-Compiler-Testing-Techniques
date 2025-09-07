
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8, bias=False)
 
    def forward(self, x1, min_value=-0.5, max_value=2.0):
        v1 = self.linear(x1)
        v2 = v1.clamp(min=min_value, max=max_value)
        return v2


# Initializing the model
m = Model()
