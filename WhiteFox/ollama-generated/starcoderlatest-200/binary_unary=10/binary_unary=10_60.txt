
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32 * 3, 64)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        v3 = relu(v2)
        return v3


# Inputs to the model
x1 = torch.randn(batch_size, 3, height * width)
