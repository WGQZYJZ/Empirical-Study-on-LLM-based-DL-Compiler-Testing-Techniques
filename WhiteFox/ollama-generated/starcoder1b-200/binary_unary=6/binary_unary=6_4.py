
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 * 64, 10)
 
    def forward(self, x):
        y = self.linear(x) - 5  # Subtract the value 5 from the output of the linear transformation
        y = relu(y)
        return y


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32 * 64 * 64)
