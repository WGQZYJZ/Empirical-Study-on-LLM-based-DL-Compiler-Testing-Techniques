
class Model(torch.nn.Module):
    def __init__(self, num_features: int):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.linear1 = torch.nn.Linear(num_features, num_features // 2)
        self.linear2 = torch.nn.Linear(num_features // 2, num_features)

    def forward(self, x):
        v0 = self.conv1(x)
        # Add a linear transformation to the input vector
        h0 = F.relu(self.linear1(v0))
        # ReLU activation to obtain new feature maps of dimension: batchsize * num_features // 2
        v1 = torch.cat([F.relu(i) for i in self.linear2(h0)], dim=-1)
        return torch.tanh(v1)


# Initializing the model
m = Model(num_features=8)


