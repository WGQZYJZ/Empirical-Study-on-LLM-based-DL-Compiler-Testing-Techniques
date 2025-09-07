
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(4096, 4096)
        self.fc2 = torch.nn.Linear(4096, 4096)
 
    def forward(self, x1, x2):
        # Concatenate two tensors along the channel dimension and return a single tensor
        v1 = torch.cat([x1, x1], dim=1)
        v2 = torch.cat([x2, x2], dim=0)
        # Get the result of matrix multiplication on concatenated tensors
        v3  = self.fc1(v1)
        v4 = self.fc2(v2)
        return torch.mm(v3, v4)


# Initializing the model
m = Model()

