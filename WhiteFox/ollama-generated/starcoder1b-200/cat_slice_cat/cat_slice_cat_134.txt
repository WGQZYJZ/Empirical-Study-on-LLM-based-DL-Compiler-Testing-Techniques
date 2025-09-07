
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1[:, 0:9223372036854775807], x2], dim=1)
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1, x2 = torch.randn(2, 3, 9, 11), torch.randn(11, 14)
