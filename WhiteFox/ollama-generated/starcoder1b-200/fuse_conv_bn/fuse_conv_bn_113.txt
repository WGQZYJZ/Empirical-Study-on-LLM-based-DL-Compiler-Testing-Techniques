
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)  # Permute the input tensor with more than two dimensions

        v2 = torch.nn.functional.conv_transpose2d(v1, self.conv.weight, self.conv.bias,
                                                    stride=self.conv.stride, padding=self.conv.padding)
        v3 = self.bn(v2)  # Batched version of a single layer: Apply batch normalization to the tensor of dimension 'x'.

        v4 = torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias)
        return v4


# Inputs to the model
x1 = torch.randn(1, 2, 2)
