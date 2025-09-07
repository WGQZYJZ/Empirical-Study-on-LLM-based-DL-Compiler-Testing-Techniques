
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 256)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        v2 = v1 + (other if other is not None else torch.tensor([0, 1]))
        v3 = torch.nn.functional.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.tensor([[0, 1]])
