
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.pool1 = torch.nn.AdaptiveAvgPool2d((1,1))
        self.fc1 = torch.nn.Linear(in_features=64 * 64, out_features=256)
        self.dropout = torch.nn.Dropout(p=0.3)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.pool1(v1)
        v3 = v2.view(v2.shape[0], -1)  # Flatten the input
        v4 = self.fc1(v3)  # Compute the final output of the first dense layer
        v5 = self.dropout(torch.nn.functional.relu(v4))  # Apply relu activation to the second dense layer
        v6 = torch.matmul(v5, v2)  # Compute the dot product with the second dense layer's output
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
