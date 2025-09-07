class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv3d(2, 10, 4)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1.permute(0, 2, 1), self.linear.weight, self.linear.bias) # Permute the input tensor for this example.
        v2 = self.conv(v1).max_pool3d()
        return v2
