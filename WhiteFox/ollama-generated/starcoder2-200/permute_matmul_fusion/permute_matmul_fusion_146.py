
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1: torch.Tensor, x2: torch.Tensor) -> torch.Tensor:
        v1  = x1.permute(0, 3, 4, 5).expand(-1,-1, -1, -1, 3, 897).reshape_as(x2)
        v2  = x2 + self._my_linear_func(v1)

        return v2

    def _my_linear_func(self, input):
         return torch.nn.functional.linear(input, self.linear.weight, self.linear.bias)

# Initializing the model
m  = Model()

