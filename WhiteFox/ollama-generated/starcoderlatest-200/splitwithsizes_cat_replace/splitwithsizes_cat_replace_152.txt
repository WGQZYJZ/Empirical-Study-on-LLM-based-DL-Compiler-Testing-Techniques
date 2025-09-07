
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_sizes = (int(v1.numel() / 2), int(v1.numel() / 2))
        concatenation_dim = -1
        split_tensors = torch.split(v1, split_sizes, dim=concatenation_dim)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=concatenation_dim)
        return concatenated_tensor


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
