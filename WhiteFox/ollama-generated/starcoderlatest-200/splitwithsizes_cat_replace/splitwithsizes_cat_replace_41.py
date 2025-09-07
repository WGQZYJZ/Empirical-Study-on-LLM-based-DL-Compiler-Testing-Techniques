
class Model(torch.nn.Module):
    def __init__(self, num_splits: int, stride: int, padding: int):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=1, stride=stride, padding=padding)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, num_splits, dim=4)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=4)
        return concatenated_tensor


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
