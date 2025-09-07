
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Permute the first input tensor with three dimensions
        v1 = x1[:, :, None]

        # Permute the second input tensor with one dimension
        v2_1d = x1[:, [0], :]
        v2_2d = torch.nn.functional.linear(v2_1d, 3)

        return self._combine(v1, v2_2d)

    def _combine(self, a: Tensor, b: Tensor):
        