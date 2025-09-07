
class Model(torch.nn.Module):
    def __init__(self, input_dim: int):
        super().__init__()
        self.fc1 = torch.nn.Linear(input_dim, 1)
 
    def forward(self, x1):
        v1  = self.fc1(x1) + 2
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3)
