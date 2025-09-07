
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-6, max_value=0.9):
        super().__init__()
        self.linear = torch.nn.Linear(8, 1)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x):
        return self.linear(torch.clamp(x, min=-self.max_value, max=self.max_value))


# Initializing the model
m = Model()


