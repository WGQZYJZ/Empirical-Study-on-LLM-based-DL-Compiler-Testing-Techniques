
class ResidualNet(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        v1 = F.relu(self.linear(x1))
        return x1 + v1


# Initializing the model
rnet = ResidualNet()
m = m  # The model should be different from the previous one.

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
