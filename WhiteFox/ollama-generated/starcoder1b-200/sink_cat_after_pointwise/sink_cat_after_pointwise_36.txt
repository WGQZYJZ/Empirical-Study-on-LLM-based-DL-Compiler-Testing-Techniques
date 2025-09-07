
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2, x3):
        v1 = x1.permute(0, 2, 1).contiguous()
        v2 = self.linear(torch.cat([x1, x2, x3], dim=-1))  # Reshape the concatenated tensor with more than two dimensions.
        return torch.relu(v2)


# Initializing the model
m = Model()


# Inputs to the model
inputs = (x1.repeat(1, 3), x1.repeat(3, 1))  # Tensor of shape (?, ?, 2). The values are arbitrary.
outputs = m(*inputs)
