
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_sizes = [256] # Split this tensor into multiple tensors along dimension dim=0 (axis=0) and use all of them in the concatenation operation
        v2 = torch.cat([v1 for i in range(len(split_sizes))], dim=0)
        return True


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
