
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-32, max_value=0):
        super().__init__()
        self.linear = torch.nn.Linear(3, 5)
 
    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1 * 0.5 + x2
        v3 = v2 * 0.7071067811865476 + min_value
        v4 = torch.clamp(v3, max_value=max_value)
        return v4


# Initializing the model
m = Model()


