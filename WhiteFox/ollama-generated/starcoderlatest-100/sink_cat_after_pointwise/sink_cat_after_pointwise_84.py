
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 3, 3)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0)
        v2 = v1.view(-1, v1.shape[1] * v1.shape[2])
        v3 = torch.nn.functional.relu(v2)  # This pointwise unary operation is applied here.
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 2, 4, 4)
