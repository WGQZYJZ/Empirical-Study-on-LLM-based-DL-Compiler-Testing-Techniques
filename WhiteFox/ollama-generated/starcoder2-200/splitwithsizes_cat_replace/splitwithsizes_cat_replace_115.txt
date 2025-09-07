
class Model(torch.nn.Module):
    def __init__(self, splitsize):
        super().__init__()
        self.splitsize = splitsize

    def forward(self, x1):
        v3  = torch.split(x1, self.splitsize) # Split the input tensor into several tensors along dimension 0. The size of each tensor is equal to `self.splitsize`.
        v4 = torch.cat([v3[i] for i in range(len(v3))], dim=0) # Concatenate the split tensors back together with concatenation operation on a new dimension (`dim` is set to 1).
        return v4


# Initializing the model
splitsize  = 64
model  = Model(splitsize)


# Input to the model: Input tensor with shape [batch size, 3, 50] for 2 splits along dimension `dim` (new dim = 1 after split, then concat with old one), where each 1/split of the original input is split into 1 tensor. Therefore there are total of 4 tensors: `[3, 64], [17, 50], [12, 50], and [8, 50]`, that will be concatenated along a new dim (dim = 1).
x1_shape  =  [batch size, 3, 50] for 2 splits along dimension `dim`

input  = torch.randn(1, 3, 50)


# Outputs of the model. The output of splitting operation is reshaped to original shape after concatenation (after concatenating we expect to get `[batch size * number of splits, new_splitsize]` where splitsize is equal to 64). Also in this model concat operation happens on a dimension that wasn't used for the splitting operation.
