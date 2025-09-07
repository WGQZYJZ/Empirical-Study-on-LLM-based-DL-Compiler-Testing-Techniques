
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.nn.functional.linear(x1.permute([0] + list(range(3))[::-1]), self.linear.weight, self.linear.bias)

# Initializing the model
m = Model()

