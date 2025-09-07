
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x):
        v1 = self.linear(x) + 1
        return relu(v1)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 28, 28)
