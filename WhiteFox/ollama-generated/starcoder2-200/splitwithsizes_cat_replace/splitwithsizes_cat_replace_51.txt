
import torch

class Model(torch.nn.Module):
    def __init__(self, split_sizes=[32]):
        super().__init__()
        self.conv = torch.nn.Conv2d(8, 10, kernel_size=5)
 
    def forward(self, x):
        output = self.conv(x)
 
        split_tensors = torch.split(output, split_sizes, dim=-1)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=-1)
        return concatenated_tensor


model = Model([32])  # Replace [32] with your desired split sizes list
inputs = torch.randn(1, 8, 64, 64)
 
output = model(inputs)

