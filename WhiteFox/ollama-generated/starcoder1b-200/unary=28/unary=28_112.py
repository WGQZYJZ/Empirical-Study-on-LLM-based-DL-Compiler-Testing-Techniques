
class Model(torch.nn.Module):
    def __init__(self, min_value=-1.0, max_value=2.0):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x):
        return self.linear(x)  # Apply a linear transformation to the input tensor


# Initializing the model
m = Model()
m.linear.weight.data.uniform_(-1.0, 2.0)
