
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
 
    def forward(self, x1, inp=None):
        v1 = self.linear1(x1)
        if inp is None:
            return v1
 
        v2 = v1 * inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 8)
inp = torch.tensor([[0.5], [1.0]])
