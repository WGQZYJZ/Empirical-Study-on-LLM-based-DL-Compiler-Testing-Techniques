
class Model(torch.nn.Module):
    def __init__(self, num_splits=16):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.num_splits = num_splits

    def forward(self, x1):
        split_sizes = [torch.tensor([64, 64]) for _ in range(self.num_splits)]  # Shape: batch x (1-dim of concatenation). Shape is fixed because the input tensor must be of shape `batch x width*height*channel`.
        concatenated_tensor = torch.cat(
            [torch.split(x1, split_sizes[i], dim) for i in range(self.num_splits)],
            dim=0
        )  # Shape: batch x num_splits*(1-dim of concatenation).

        return True


# Initializing the model
m = Model()

__input__ = torch.randn(1, 3, 64, 64)
output = m(__input__)  # Outputs is True
assert output == __output__  # If `return True`, we should expect `output` to be `True`.


