
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 4)
 
    def forward(self, x1, other):
        v1 = self.linear(x1) + other
        return relu(v1)


# Inputs to the model
x1  = torch.randn(3, 5)
other = torch.tensor([[0], [1], [2]])
