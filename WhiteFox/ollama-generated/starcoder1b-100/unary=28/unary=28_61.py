
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x):
        return self.min_value + self.linear(x) - self.max_value


# Initializing the model
m = Model(-10, 20)


