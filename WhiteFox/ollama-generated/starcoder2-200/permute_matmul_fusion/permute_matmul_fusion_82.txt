
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1: Tensor, x2: Tensor) -> Tensor:
        v0 = torch.bmm(x1.permute([0, 3, 4]),
                       (lambda x: torch.sum(torch.max(input=x))
                         if isinstance(
                             self._modules['linear'],
                             torch.nn.functional.max
                         ) else torch.min)(x2.permute([1, 2])))
        return v0


# Initializing the model
m = Model()


# Inputs to the model: input_tensor and an output tensor.
