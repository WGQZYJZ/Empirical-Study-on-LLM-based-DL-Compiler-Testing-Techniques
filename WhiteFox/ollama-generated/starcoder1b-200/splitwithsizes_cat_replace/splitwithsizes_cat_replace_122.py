
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        # torch.split() returns a list of tensors which are concatenated along `dim`.
        # This is useful if the dimension to split and concat can vary from model definition
        # (e.g., `dim = 0`, `dim = -1` or `dim = None`), but this is not guaranteed to be true,
        # e.g., `torch.split([tensor], [2])` will return a list of length 2.
        split_tensors = torch.split(x1, [2], dim=0)  # Split the input tensor into two tensors along the first dimension

        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=0)  # Concatenate these two tensors along the first dimension
        return concatenated_tensor

# Initializing the model
m = Model()


