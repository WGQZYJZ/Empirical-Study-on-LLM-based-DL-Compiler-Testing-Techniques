
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.cat([tensor1, tensor2, ...], dim=...)  # Concatenate tensors along a dimension
        t3 = t1.view(...)  # Reshape the concatenated tensor
        return torch.relu(t3)


# Initializing the model
m = Model()

