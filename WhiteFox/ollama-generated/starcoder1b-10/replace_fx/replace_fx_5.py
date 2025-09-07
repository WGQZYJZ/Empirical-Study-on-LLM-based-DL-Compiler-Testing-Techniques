
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.rand_like(v1, ...) # Generate a tensor with the same size as input_tensor filled with random numbers
        return torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)

# Initializing the model
m = Model()

