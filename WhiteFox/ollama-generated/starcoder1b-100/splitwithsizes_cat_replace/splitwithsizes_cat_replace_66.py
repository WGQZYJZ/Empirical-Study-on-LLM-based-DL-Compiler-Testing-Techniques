
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return self._split_tensors(x1)[0] + 1

    @staticmethod
    def _is_valid_splitwithsizes_cat(tensor: torch.Tensor, split_sizes: Sequence[int]) -> bool:
        assert len(split_sizes) == 2
        assert isinstance(tensor, torch.Tensor)
        assert tensor.ndim == 3
        assert isinstance(split_sizes, Sequence)
        return True


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
