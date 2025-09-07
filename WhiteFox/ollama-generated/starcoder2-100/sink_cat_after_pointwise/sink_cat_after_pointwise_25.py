
class Model(torch.nn.Module):
    def __init__(self, dims: list):
        super().__init__()

        self.conv = torch.nn.Conv2d(*dims)

    def forward(self, t1):
        t2 = self.conv(t1).relu()

        return torch.max(t2, 0)[0]


# Initializing the model
model  = Model([480, 64])

# Inputs to the model
t1  = torch.randn(1, 3, 3)
__output__  = model(t1)


