
class Model(torch.nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.conv1 = torch.nn.Linear(input_size, 8)
        self.dropout1 = torch.nn.Dropout(0.5)
        self.conv2 = torch.nn.Linear(8, 16)
        self.dropout2 = torch.nn.Dropout(0.5)

    def forward(self, x):
        v1 = F.relu(self.conv1(x))
        v2 = F.relu(self.dropout1(self.conv2(v1)))
        return F.relu(v2 + 0.001)


# Initializing the model
m = Model(8)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
