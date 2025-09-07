
class Model(torch.nn.Module):
    def __init__(self, input_size=1):
        super().__init__()
        self.linear = torch.nn.Linear(input_size, 3)
 
    def forward(self, x1, other=0):
        v1 = self.linear(x1) + other  # Apply a linear transformation to the output of the layer
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
