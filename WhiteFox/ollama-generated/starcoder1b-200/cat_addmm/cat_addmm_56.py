
class Model(torch.nn.Module):
    def __init__(self, x_dim: int = 10, y_dim: int = 8):
        super().__init__()
        self.fc1 = torch.nn.Linear(x_dim, y_dim)
 
    def forward(self, x):
        v = self.fc1(x)
        return v


# Initializing the model
m = Model()

