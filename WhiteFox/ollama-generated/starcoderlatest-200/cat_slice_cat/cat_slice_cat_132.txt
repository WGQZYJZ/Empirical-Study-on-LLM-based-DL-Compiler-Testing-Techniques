
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.concat = torch.cat

    def forward(self, x1, x2, x3):
        t1 = self.concat([x1, x2], dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:size]
        t4 = self.concat([t1, t3], dim=1)
        return t4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
x3 = torch.randn(1, 2049, 64, 64)
