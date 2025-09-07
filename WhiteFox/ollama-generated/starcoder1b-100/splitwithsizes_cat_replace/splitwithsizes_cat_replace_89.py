
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=2, padding=1)
 
    def forward(self, x1):
        split_tensor1 = self.conv1(x1)  # Split the input tensor into several tensors along a given dimension
        split_tensor2 = torch.split(split_tensor1, [64 * 3 * 4], dim=0)[0]
        concatenated_tensor = torch.cat([split_tensor2, self.conv2(x1)], dim=0)  # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Initializing the model
m = Model()
