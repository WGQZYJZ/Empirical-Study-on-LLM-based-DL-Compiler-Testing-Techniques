
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32)
 
    def forward(self, x1):
        return self.linear(x1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64, requires_grad=True)
output = m(x1)
print("x1: ", x1)
print("output: ", output)


