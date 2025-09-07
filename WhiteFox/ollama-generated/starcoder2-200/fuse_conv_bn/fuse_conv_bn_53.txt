
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.conv2d(x1, conv3x3.weight)
        v4 = torch.nn.functional.batch_norm2d(v2) # BatchNorm should track running stats
        return 0


# Initializing the model
m = Model()

# Inputs to the model:
x1 = torch.randn(1, 3, 32, 32)


# 