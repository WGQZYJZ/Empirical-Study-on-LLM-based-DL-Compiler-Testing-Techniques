
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = v1 * -1 # Create a boolean tensor where each element is True if the corresponding element in v1 is greater than 0, and False otherwise
        v3 = v1 * -0.5 # Multiply the output of the linear transformation by the negative slope
        return torch.where(v2, v1, v3)


# Initializing the model
m = Model()

