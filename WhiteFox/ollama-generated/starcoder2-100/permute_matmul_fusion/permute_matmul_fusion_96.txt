
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1: torch.Tensor, x2: torch.Tensor) -> torch.Tensor:
        v3 = x1  # or x2, or both (your choice of inputs)
        v4 = self._apply_linear_to_tensor(v3)

        return v4

    def _apply_linear_to_tensor(self, t1):
        t2 = torch.nn.functional.linear(t1.permute(-1,-2), torch.randn(2, 1))
        return t2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3,4)
x2 = torch.randn(4,3)
