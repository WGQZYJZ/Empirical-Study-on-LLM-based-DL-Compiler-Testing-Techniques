
class Model(torch.nn.Module):
    def __init__(self, feature_dim=100):
        super().__init__()
        self.linear = torch.nn.Linear(feature_dim, feature_dim)

    def forward(self, x1, x2, x3, x4, x5):
        # Concatenate the five tensors and view the concatenated tensor as a single vector
        z = torch.cat([x1, x2, x3, x4, x5], dim=1)  # ... or z = torch.cat(tuple(t1, t2, t3, t4, t5))

        # Reshape the concatenated tensor to a single vector
        v1  = torch.reshape(z, -1)
        v2 = self.linear(v1).view(self.linear.in_features // x1.shape[1], x1.shape[0])
        return torch.relu(v2)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 4)
x2 = torch.randn(1, 3, 3)
x3 = torch.randn(1, 2, 2)
x4 = torch.randn(1, 1, 1)
x5 = torch.randn(1, 3, 3)
