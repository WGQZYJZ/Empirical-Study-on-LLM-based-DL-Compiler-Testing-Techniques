
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        split_tensor_0, _ ,split_tensor_1 = torch.split(v1, [4,2], dim=1)
        concatenated_tensor = torch.cat([split_tensor_0, split_tensor_1], dim=1)  # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
