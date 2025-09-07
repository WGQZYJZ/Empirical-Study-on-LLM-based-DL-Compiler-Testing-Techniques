
class Model(torch.nn.Module):
    def __init__(self, kernel_size, stride, padding):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=kernel_size, stride=stride, padding=padding)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [3, 3, 3], dim=1) # Split the input tensor into three tensors along dim=1
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=1) # Concatenate the split tensors along dim=1
        return concatenated_tensor


# Initializing the model
m = Model()

