
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        v1 = torch.nn.functional.linear(x, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 2, 1) # Use permute on the output tensor of linear transformation. 
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(3, 10, 4)
