
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, x1, 0 * v1) # Create a boolean tensor where each element is True if the corresponding element in v1 is greater than 0, and False otherwise
        v3 = -v2  # Multiply negative slope with the output of linear transformation
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
