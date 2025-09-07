
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split_tensor1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, split_sizes=[3], dim=0)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=0)
        return concatenated_tensor
