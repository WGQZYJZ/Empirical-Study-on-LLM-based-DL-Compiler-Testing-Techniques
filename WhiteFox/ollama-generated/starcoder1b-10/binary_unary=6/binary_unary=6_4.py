
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 128 * 128, 512)

    def forward(self, x):
        v = torch.randn((x.size(0), x.shape[1]))
        return self.linear(v)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 64 * 128 * 128)
