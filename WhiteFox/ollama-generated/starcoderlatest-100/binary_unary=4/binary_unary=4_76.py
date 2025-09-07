
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None):
        if (other is None):
            other = torch.randn(8)
        v1 = self.linear(x1) + other
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

 # The 'other' tensor is passed as a keyword argument
