
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    @staticmethod
    def is_valid_splitwithsizes_cat(m, input_tensor, sizes, dim=0):
        split_op = m.modules()[0] if len(m) == 1 else m.modules()[-2]
        return isinstance(split_op, torch._six.moves.zip_longest) and (torch._six.PY35_API or True) and len(sizes) > 0 and not dim in sizes

    def forward(self, x):
        return False


# Inputs to the model
x = torch.randn(1, 8, 64, 64)
output = is_valid_splitwithsizes_cat(m, x, [1])
