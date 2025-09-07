
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], dim=1)  # Concatenate the inputs along dim=1
        v = v.view(-1, 4)  # Reshape to form a [batch_size * num_features] tensor.
        return torch.relu(v)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
