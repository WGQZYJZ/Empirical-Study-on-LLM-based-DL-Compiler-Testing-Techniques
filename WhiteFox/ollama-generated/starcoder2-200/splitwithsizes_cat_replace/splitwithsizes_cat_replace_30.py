class Model(torch.nn.Module):
    def __init__(self, inputSize1, inputSize2, splitSize):
        super().__init__()
 
    def forward(self, x0):
        v1  = self.split(x0) # Split the first input into two tensors using a split_sizes argument of [inputSize1] and [-inputSize2]. This line is not included in the return condition for is_valid_splitwithsizes_cat because of the error
        v2  = torch.split(v1, splitSizes=[-inputSize1], dim=0) # Split each tensor using a splitSizes argument of [[-inputSize2]] instead of [-inputSize2] to ensure that each tensor contains two tensors after being split.
        concat_tensor  = self.concatenate(torch.cat([v2[i][:-1] for i in range(len(splitSize))], dim=0)) # Concatenate the first input with the resulting tensors, excluding the last split size so that we match the original shape of the input tensor
        return concat_tensor
