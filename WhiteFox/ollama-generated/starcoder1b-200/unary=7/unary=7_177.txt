
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 6, bias=True)
 
    def forward(self, x1):
        l1 = self.linear(x1)
        return clamp(l1 + 3, 0, 6, l1 + 3) / 6


# Initializing the model
m  = Model()


