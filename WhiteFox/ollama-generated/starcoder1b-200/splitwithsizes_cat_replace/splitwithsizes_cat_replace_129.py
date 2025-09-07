
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    @staticmethod
    def is_valid_splitwithsizes_cat(tensor):
        return not tensor.ndim < 2 or len(tensor.shape) - 1 == sum([s >= 0 for s in tensor.shape[:-1]])

    def forward(self, x):
        input_tensor = x
        if not self.is_valid_splitwithsizes_cat(input_tensor):
            split_sizes = [5] * len(x.shape)
            concatenated_tensor = torch.cat([input_tensor for _ in range(len(split_sizes))], dim=-1)
        else:
            split_sizes = input_tensor.shape[:-1]
            concatenated_tensor = input_tensor
        return concatenated_tensor


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
