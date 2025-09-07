
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return torch.functional.conv_nd(x1, self.linear.weight, self.linear.bias)

# Initializing the model
m = Model()


