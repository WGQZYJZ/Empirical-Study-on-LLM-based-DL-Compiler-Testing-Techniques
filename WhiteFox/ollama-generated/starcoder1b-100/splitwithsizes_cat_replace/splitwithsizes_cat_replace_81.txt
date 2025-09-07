
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        split_tensors, split_sizes = self._split_tensor_and_sizes(x1)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=0)  # Split the input tensor into several tensors along a given dimension
        return concatenated_tensor

    def _split_tensor_and_sizes(self, x1):
        split_sizes = [torch.tensor(64), torch.tensor(128)]  # All split sizes are used in the concatenation operation and all of them are different (64). The order of the split tensors in the concatenation operation is the same as their original order in the split operation.
        split_tensors = [torch.chunk(x1, split_sizes[i], dim=0) for i in range(len(split_sizes))]  # Split the input tensor into several tensors along a given dimension. Note that we only need to process each chunk and then concatenate them together later.
        return split_tensors, split_sizes


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
