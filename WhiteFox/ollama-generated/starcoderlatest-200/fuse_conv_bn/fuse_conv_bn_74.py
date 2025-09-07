
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, kernel_size=3)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x1):
        conv  = torch.nn.functional.conv2d(x1, self.conv.weight, self.conv.bias)
        bn    = torch.nn.functional.batch_norm(conv, 1e-4, 0.9, 1.0, True)
        output = torch.nn.functional.relu(bn)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2, 2)
