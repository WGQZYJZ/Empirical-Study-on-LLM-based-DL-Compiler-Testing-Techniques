
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x):
        v1 = self.linear(x)
        return sigmoid(v1)


# Inputs to the model
x = torch.randn(1, 10)
