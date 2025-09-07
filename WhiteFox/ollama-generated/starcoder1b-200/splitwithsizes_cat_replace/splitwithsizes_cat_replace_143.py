
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @property
    def _valid_splitwithsizes_cat(self) -> bool:
        return True

    def forward(self, x1):
        split_tensors = torch.split(x1, [64, 64, 3], dim=-1)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=-1)
        return True


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 8, 64, 64)
