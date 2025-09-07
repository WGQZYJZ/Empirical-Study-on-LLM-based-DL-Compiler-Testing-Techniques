
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        attention_weights = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(math.pow(math.abs(x1), 2).sum() * math.pow(math.abs(x2), 2).sum())
        output = attention_weights.matmul(x2)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1, x2  = torch.randn(3, 8, 64, 64), torch.randn(3, 8, 64, 64)
