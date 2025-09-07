
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        l = self.linear(x) + 3
        return torch.clamp(l, min=0, max=6), torch.clamp(l, min=-6, max=0)


# Initializing the model
m = Model()


