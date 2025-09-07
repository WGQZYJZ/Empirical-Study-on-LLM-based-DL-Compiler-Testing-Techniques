
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Linear(50, 20)
        self.layer2 = torch.nn.Linear(20, 10)

    def forward(self, x1, x2):
        y1 = self.layer1(x1)
        y2 = self.layer2(x2)
        attention_weights = torch.softmax((y1 @ y2.transpose(-1, -2)) / math.sqrt(y2.size(-1)), dim=-1)  # y2 / (|y2| sqrt(dim=1)) @ (y1^T y2).t()
        return attention_weights.matmul(y2)


# Initializing the model
m = Model()


# Inputs to the model
x1, x2 = torch.randn(40, 50), torch.randn(40, 30)
