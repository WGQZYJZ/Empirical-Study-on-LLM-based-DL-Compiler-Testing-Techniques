
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1) + (other if other is not None else torch.zeros_like(v1))
        v2 = torch.nn.functional.relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
