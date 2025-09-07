
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8, bias=False)
        self.clamp = lambda x: min(6, max(0, x))
 
    def forward(self, x):
        l = self.linear(x)
        m = l * self.clamp(l + 3) / 6
        return m


# Initializing the model
m = Model()

