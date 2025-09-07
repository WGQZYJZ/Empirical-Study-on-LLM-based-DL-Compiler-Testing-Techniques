
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=2, padding=1)
 
    def forward(self, x1):
        split_sizes = [1, 5]
        concatenated_tensor  = torch.cat([self.conv1(x1[:, :, i:i+5]), self.conv2(split_tensors[1](x1)) for i in range(len(split_sizes))], dim=1)
        