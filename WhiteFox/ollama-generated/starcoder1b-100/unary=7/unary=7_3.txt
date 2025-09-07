
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 * torch.clamp(min=0, max=6, l1 + 3) / 6


# Initializing the model
m = Model()
