
class Model(torch.nn.Module):
    def __init__(self, min_value=0.1, max_value=3.5):
        super().__init__()
        self.linear = torch.nn.Linear(4, 2)
 
    def forward(self, x):
        v = self.linear(x)
        return torch.clamp(v, min=min_value, max=max_value)


# Initializing the model
m = Model()


