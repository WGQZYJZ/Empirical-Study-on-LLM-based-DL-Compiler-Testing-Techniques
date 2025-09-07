
class Model(torch.nn.Module):
    def __init__(self, min_value=0.31864529670951346, max_value=0.7401307954980387):
        super().__init__()
        self.linear = torch.nn.Linear(1, 2)
 
    def forward(self, x):
        return self.linear(x) * (max_value - min_value) + min_value


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(100, 100) * 30
