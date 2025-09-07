
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 7 * 2, 10)
 
    def forward(self, x1):
        v1 = torch.cat((x1.view(1, -1), x1.view(-1, 64*7*2)), dim=1)  # Concatenate the first and second input (flattened to 1-dimensional tensor) into one tensor for matrix multiplication
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64*7*2)
