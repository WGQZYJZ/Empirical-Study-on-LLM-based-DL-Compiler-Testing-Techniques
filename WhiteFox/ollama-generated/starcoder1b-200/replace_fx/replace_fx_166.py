
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return dropout_like(x1, fallback_random=False), dropout_like(self.linear.weight, fallback_random=False), dropout_like(self.linear.bias, fallback_random=True)


# Initializing the model
m = Model()


