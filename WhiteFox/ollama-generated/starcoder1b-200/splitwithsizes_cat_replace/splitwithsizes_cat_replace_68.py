
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        split_sizes = (v1.shape[0] * 2,)
        concatenated_tensor = torch.cat([torch.split(input_tensor, split_sizes, dim) for input_tensor in [v1]], dim)
        return concatenated_tensor


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
