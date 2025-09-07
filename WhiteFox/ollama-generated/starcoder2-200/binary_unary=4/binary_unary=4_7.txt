
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return torch.relu(v1 + other)

# Initializing the model
m  = Model()

# Inputs to the model