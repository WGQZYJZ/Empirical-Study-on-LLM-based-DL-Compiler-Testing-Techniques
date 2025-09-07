
class Model(torch.nn.Module):
    def __init__(self, n1: int = 3, n2: int = 4):
        super().__init__()
        self.fc1 = torch.nn.Linear(n1, n2)
 
    def forward(self, x1, x2):
        v1 = self.fc1(x1)
        v2 = torch.cat([v1, x2], dim=-1)  # Concatenate two tensors along a specified dimension
        return v2


# Initializing the model
m = Model()


