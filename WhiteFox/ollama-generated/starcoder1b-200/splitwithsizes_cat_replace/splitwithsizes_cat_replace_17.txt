
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @staticmethod
    def is_valid_splitwithsizes_cat(splits, sizes):
        return splits == torch.unsqueeze(torch.stack([torch.split(x, [s], dim) for s, x in zip(sizes, splits)]), dim=0)


# Inputs to the model
x1 = torch.randn(3, 4, 64, 64)
splits, sizes = Model.is_valid_splitwithsizes_cat(x1, [2, 4])  # Split x1 into two tensors of sizes 2 and 4
