
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.split_tensors = torch.split(input_tensor, [4]*3, dim) # Split 0-1-2 into 3 parts along axis dim
        self.concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim)
 
    def forward(self, x):
        return v6


