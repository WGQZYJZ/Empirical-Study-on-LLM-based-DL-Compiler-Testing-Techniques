
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
 
    def forward(self, x):
        v = self.linear(x)
        return torch.clamp(v, min_value, max_value)


# Initializing the model
m = Model()

