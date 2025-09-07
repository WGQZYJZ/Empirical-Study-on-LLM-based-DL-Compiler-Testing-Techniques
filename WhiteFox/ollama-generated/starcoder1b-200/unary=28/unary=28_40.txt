
class Model(torch.nn.Module):
    def __init__(self, min_value=-1.0, max_value=1.0):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x):
        return self.linear(x).clamp_(min=self.min_value, max=self.max_value)


# Initializing the model
m = Model(min_value=-100, max_value=100)
