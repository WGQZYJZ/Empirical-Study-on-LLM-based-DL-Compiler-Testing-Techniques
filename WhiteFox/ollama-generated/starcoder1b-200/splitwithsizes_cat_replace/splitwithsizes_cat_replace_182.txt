
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        split_sizes = [64, 256, 512, 512] # [input_tensor1], [input_tensor2], [input_tensor3], [input_tensor4]
        concatenated_tensor = torch.cat([torch.split(v1, split_sizes[i], dim) for i in range(len(split_sizes))], dim)  # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
