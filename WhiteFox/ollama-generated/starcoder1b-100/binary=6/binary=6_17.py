
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1) - x1  # Subtract the input tensor from the output of the linear transformation
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
other = 0.5
