
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 3)

    def forward(self, x1):
        v1 = F.relu(F.conv2d(x1, self.conv.weight))
        v2 = F.batch_norm(v1, v1, self.conv.bias, self.conv.running_mean, self.conv.running_var)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 28, 28)
