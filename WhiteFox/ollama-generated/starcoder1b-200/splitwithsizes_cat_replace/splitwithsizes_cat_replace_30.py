
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes  = [4]  # We expect the first output of the convolution to be split into four tensors, and then each tensor in turn should have a length of 6. If that is not the case, then there will be a problem.
        concatenated_tensor  = torch.cat([torch.split(x1, split_sizes, dim=0)[i] for i in range(len(split_sizes))], dim=0)
        return concatenated_tensor
