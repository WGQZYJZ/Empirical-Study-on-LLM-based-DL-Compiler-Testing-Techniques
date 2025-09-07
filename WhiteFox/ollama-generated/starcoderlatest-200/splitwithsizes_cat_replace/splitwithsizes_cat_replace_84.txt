
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        split_tensors = torch.split(x1, split_sizes=4, dim=3)  # Split along the dimension with size 4
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=3)  # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
