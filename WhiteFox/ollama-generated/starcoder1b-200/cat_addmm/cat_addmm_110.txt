
class Model(torch.nn.Module):
    def __init__(self, in_features: int = 64):
        super().__init__()
        self.fc1 = torch.nn.Linear(in_features, 32)
        self.fc2 = torch.nn.Linear(32, 1)
 
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x1  = self.fc1(x) # Vectorization (for better performance)
        x2  = self.fc2(x1)
        return x2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
