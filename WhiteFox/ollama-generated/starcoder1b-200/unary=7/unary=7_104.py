
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = v1 * clamp(min=0, max=6, v1 + 3)
        return v2 / 6


# Initializing the model
m = Model()

