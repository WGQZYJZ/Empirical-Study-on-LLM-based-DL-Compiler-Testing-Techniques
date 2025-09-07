
class Linear(torch.nn.Module):
    def __init__(self, out_features=32, bias=True):
        super().__init__()
        self.linear = torch.nn.Linear(3, out_features)

    def forward(self, x1, **other):
        return relu(self.linear(x1))


# Initializing the model
m = Linear()


