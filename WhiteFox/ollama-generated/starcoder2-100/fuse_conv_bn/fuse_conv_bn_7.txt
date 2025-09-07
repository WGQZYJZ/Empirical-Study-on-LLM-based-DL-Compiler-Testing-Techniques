
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        # conv1: 4x3x3, 24
        self.conv1 = torch.nn.Conv2d(4, 24, kernel_size=5)
        # batchnorm1: 24
        self.batchnorm1 = torch.nn.BatchNorm2d(24)

    def forward(self, x):
        x = self.conv1(x)

        if (not self.training and not self.batchnorm1.training
            or self.batchnorm1._modules["momentum"] == 0.99):
            # Conv1 is fused with batch norm1 when it matches the above pattern

            # BN1 will be removed from the graph, resulting in no additional memory usage
            x = self.batchnorm1(x)
            return x

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(10,4,32,32)

# Running the model in eval mode with batch norm tracking statistics
torch.set_grad_enabled(False)
with torch.no_grad():
    m.train()
    m.eval()
    __output__  = m(x)

