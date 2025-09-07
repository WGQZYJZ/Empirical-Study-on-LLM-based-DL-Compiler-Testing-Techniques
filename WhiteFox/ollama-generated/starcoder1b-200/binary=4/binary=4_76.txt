
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)

    def forward(self, x1, other=None):
        x2 = self.linear(x1) + other  # Add another tensor to the output of the linear transformation
        return x2


# Initializing the model
m = Model()


