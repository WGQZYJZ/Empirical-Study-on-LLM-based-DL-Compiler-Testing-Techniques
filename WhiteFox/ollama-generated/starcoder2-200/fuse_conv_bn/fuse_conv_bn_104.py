
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5) # Conv2d(in_channels=3, out_channels=8, kernel_size=5, dilation=1)
        self.conv2 = torch.nn.Conv2d(8, 10, 4) # Conv2d(in_channels=8, out_channels=10, kernel_size=4, dilation=1)

    def forward(self, x):
        output = x.permute(0, 3, 1, 2)
        v1 = torch.nn.functional.conv2d(output, self.conv1.weight, bias=None, stride=1, padding=0, dilation=1) # conv2d: 4D Tensor, 8D Tensor, 5D Tensor
        v2 = torch.nn.functional.relu(v1) # Relu: 8D Tensor
        v3 = torch.nn.functional.conv2d(output, self.conv2.weight, bias=None, stride=1, padding=0, dilation=1) # conv2d: 4D Tensor, 10D Tensor, 4D Tensor
        return torch.nn.functional.batch_norm(v3 + v2)


# Initializing the model
m = Model()


