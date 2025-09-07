
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], dim=0) # Concatenate tensor with 0th dimension
        v = v.view(-1, 4, 2)     # Reshape the concatenated tensor to [batch_size, number of points * 4, input_dim]
        return torch.relu(v)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 3, 2)
x2 = torch.randn(5, 6, 2)
