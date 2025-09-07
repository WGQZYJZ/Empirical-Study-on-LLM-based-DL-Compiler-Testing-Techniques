
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64, 10)
 
    def forward(self, x):
        v1 = self.linear(x) - 5 # Subtract a certain value (referred to as 'other') from the output of the linear transformation
        return relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(64 * 64)
