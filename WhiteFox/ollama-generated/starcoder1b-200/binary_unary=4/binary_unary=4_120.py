
class Model(torch.nn.Module):
    def __init__(self, other=1):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x, other=1):
        v1 = self.linear(x) + other  # Add another tensor to the output of the linear transformation
        v2 = self.relu(v1)         # Apply the ReLU activation function to the result
        return v2


# Initializing the model
m = Model()
__input__ = torch.randn(4, 3, 64, 64)
other = torch.ones(4, 2)
x  = m(__input__, other)


