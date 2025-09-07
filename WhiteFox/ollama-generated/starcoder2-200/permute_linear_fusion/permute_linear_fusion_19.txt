
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = x1.permute([0] + list(range(x1.dim()))[:-2]) # The permute is applied on a 3-dimension input tensor.
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2

# Initializing the model