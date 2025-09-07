
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        output_tensor = self.conv(x1)  # The input tensor split into two tensors along the dimension "2"
        return torch.split(output_tensor, 2, dim=2)[0]


# Inputs to the model
x1 = torch.randn(3, 64, 64)  # Each row represents a split of the input tensor with 2 elements along the dimension "1"
