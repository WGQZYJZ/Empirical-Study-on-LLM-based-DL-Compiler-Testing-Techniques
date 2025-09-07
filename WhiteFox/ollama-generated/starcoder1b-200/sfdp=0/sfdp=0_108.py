
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.norm1 = torch.nn.LayerNorm(8)

    def forward(self, x1):
        w1 = self.norm1(self.conv1(x1))
        w2 = torch.matmul(w1, w1) / math.sqrt(math.log(float(len(w1)))) * 0.70710678118654755
        return w2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
