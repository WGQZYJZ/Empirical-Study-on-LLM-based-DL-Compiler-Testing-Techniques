
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.weight, self.bias)
        return v1  # The output of the model is already in the last two dimensions.


# Initializing the model
m = Model()
