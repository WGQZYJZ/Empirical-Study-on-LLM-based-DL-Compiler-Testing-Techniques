
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(250, 84)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = torch.mm(x1[:, :, :3], x1[:, :, -3:]) + x1
        v2  = torch.cat([v1 for _ in range(5)]) # The number of times the matrix multiplication result is concatenated depends on the length of the list in torch.cat().
        return self.relu(self.linear(x1))


# Initializing the model