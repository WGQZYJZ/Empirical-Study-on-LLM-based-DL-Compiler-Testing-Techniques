
class Model(torch.nn.Module):
    def __init__(self, n_splits=5, input_size=64):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        split_tensors = torch.split(x1, n_splits, dim=0) # Split the input tensor into several tensors along a given dimension
        concatenated_tensor = torch.cat([split_tensor for split_tensor in split_tensors], dim=0) # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Initialization of model with n_splits as 5, input size as 64.
m = Model(n_splits=5, input_size=64)
x1 = torch.randn(1,3,input_size,input_size)
