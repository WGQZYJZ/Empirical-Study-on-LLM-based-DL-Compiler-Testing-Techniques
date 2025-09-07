
class Model(torch.nn.Module):
    def __init__(self, other_tensor):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 5)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1) + other if other else self.linear(x1)
        return relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2)
