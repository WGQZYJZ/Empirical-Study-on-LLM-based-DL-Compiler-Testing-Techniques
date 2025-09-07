
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        # Rearrange the input tensors along batch and feature dimensions
        v1 = x1.permute(0, 2, 1)  # Batch dim first then feature dim
        v2 = torch.cat([x1, x2], dim=2).view(-1, 2)  # Reshape the concatenation tensor
        # Apply pointwise linear transformation to the reshaped input tensors
        v3 = self.linear1(v1)  # Pointwise linear transform to the reshaped input tensors
        v4 = self.linear2(v2)  # Pointwise linear transform to the reshaped input tensors
        return torch.cat([v3, v4], dim=1).view(-1)

# Initializing the model
m = Model()


