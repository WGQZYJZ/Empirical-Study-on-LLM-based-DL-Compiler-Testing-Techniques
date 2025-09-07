
class Model(torch.nn.Module):
    def __init__(self, min_value=-10, max_value=20):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * 0.7
        v3 = v2 + min_value
        v4 = v3 + max_value
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 10)
