
class Model(torch.nn.Module):
    def __init__(self, min_value=-5.0, max_value=10.0):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
        self.min_value  = min_value
        self.max_value  = max_value
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + torch.clamp((v1 + 2), self.min_value, self.max_value)


# Initializing the model
m = Model()


