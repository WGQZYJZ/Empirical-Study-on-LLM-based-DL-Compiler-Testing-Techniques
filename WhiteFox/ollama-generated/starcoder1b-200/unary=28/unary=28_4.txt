
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=2.):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        return self.linear(torch.clamp_(x1, min=self.min_value, max=self.max_value))


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4)
