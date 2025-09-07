
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(50, 128)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 - other # Replace with the actual value you find in the input.
        return relu(v2)


# Initializing the model
m = Model()


# Inputs to the model