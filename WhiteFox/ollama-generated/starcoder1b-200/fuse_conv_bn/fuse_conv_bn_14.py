
class Model(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...) # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNormXd(...) # X should match with ConvXd
        self.fc   = torch.nn.Linear(hidden_size * hidden_size, 1)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 3, 1).contiguous()
        v2 = self.conv(v1)
        v3 = self.bn(v2)
        return self.fc(v3)


# Initializing the model
m = Model(hidden_size=256)

