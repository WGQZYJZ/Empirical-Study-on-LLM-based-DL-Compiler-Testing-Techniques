
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0  = torch.split(x1, [32], dim=1)[-1] # Split the input tensor along dimension `dim` into three tensors. The size of each split is given by the corresponding entry in the split_sizes list (i.e., for dim == 1 it will return a list with two elements containing tensors of sizes `[32, 64]`).
        v0_out  = self._splitwithsizes(v0) # Apply the _splitwithsizes function to the input tensor `v0`
        v1  = torch.cat([v0[i][j] for i in range(len(self._splitwithsizes.__annotations__["split_sizes"])) for j in range(v0_out[i].shape[-1])], dim=1) # Concatenate the split tensors along dimension `dim`
        v2  = self.conv1(v1) + 1 
        return v2

    def _splitwithsizes(self, x):
      if isinstance(x, torch.Tensor):
        splitsizes = [32]
      else:
        raise TypeError('expected input to be a Tensor')
      dim = 0

      return tuple([torch.split(x_, split_, dim=dim) for (x_, split_) in zip(tuple(splitsizes), x)])
