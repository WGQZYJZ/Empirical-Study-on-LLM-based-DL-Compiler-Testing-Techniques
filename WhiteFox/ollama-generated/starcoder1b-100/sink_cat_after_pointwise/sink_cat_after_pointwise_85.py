
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.cat([v1, x2], dim=1)  # Concatenate tensors along the first dimension
        return torch.relu(torch.nn.functional.linear(v2, self.linear.weight, self.linear.bias))


# Initializing the model
m = Model()

