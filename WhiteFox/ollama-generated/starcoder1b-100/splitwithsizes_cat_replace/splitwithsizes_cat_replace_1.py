
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [256, 256], dim=1)  # Split the input tensor into two tensors along a dimension of size 256
        concatenated_tensor = torch.cat([
            split_tensors[i] for i in range(len(split_sizes))], dim=1)  # Concatenate the split tensors along a dimension of size 256
        concatenated_tensor_conved = self.conv1(concatenated_tensor)  # Convolve both tensors with the same stride and padding and obtain their respective outputs for conv1
        return self.conv2(concatenated_tensor_conved)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
