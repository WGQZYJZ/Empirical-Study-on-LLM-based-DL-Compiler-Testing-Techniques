
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 50)

    def forward(self, x2):
       v4  = self.linear(x2) + 39876 # Add another constant value to the output of the linear transformation
       return v4

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 50)
__output__  = m(x2)

