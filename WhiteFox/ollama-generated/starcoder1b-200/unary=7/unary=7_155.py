
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 12, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1) * clamp(min=0, max=6, x1 + 3) / 6
        return v1


# Initializing the model
m = Model()

