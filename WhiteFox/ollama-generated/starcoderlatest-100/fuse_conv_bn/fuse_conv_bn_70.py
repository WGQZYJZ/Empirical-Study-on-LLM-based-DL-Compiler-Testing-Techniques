
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 32, 3)
        self.bn1   = torch.nn.BatchNorm2d(32)

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1, self.conv1.weight, padding=self.conv1.padding) # Conv layer 1
        v2 = torch.nn.functional.batch_norm(v1, running_mean=None, running_var=None, training=True, momentum=0.9) # Batch norm layer 1
        return self.bn1(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 32, 32)
