
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = F.conv2d(...)
        bn = torch.nn.functional.batch_norm(...)
        output = F.relu(bn(v1))
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 4, 4)
