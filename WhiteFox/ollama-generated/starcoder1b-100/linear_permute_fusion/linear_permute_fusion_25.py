
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.nn.functional.relu(v1)

    def linear(self, input_tensor):
        v1  = input_tensor.permute(0, 2, 1)
        v2  = torch.nn.functional.linear(v1, self.weight, self.bias)
        return v2


# Initializing the model
m = Model()
m.linear.weight = ... # This is used to initialize m.linear.weight
