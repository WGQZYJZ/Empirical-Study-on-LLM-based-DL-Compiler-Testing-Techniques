 with optimization enabled
class Model_o(torch.nn.Module):
    def __init__(self, opt_level=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if opt_level == 2:
            from torch import distributed as dist
            rank = dist.get_rank()
            group = dist.group_from_backend("nccl")
            self._dist_init_(group, rank)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, 2, dim=1)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=1)
        