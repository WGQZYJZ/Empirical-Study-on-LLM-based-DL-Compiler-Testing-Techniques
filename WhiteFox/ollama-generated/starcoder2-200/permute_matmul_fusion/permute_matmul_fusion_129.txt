
class Model(torch.nn.Module):
    def __init__(self, batchSize):
        super().__init__()
        self.linear = torch.nn.Linear(20, 3)

    def forward(self, x1):
        v1 = x1[:, :, :5] # Permute the first 4 dimensions of the input tensor. 
        v2 = x1[:, :, -6:]# Permute the last 6 dimensions of the input tensor. 
        t1 = torch.bmm(v1, self.linear.weight)
        return torch.cat([t1, v2], dim=2).sum()


# Initializing the model