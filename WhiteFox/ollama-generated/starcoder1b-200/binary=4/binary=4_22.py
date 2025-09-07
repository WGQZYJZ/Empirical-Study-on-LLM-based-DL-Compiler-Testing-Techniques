
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(500, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 3  # Add a tensor to the output of the linear transformation
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 500)
