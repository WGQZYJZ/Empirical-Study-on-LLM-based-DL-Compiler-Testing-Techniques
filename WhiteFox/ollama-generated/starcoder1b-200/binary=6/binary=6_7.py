
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) - x1  # Subtract the output of the linear transformation from the input tensor
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 256)
