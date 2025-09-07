
class Model(torch.nn.Module):
    def __init__(self, split_sizes=[], dim=0):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.split(x1, split_sizes, dim) # split input to multiple tensors along the given dimension of input tensor.
        return torch.cat([v2 for v2 in v1], dim=dim)


m  = Model(split_sizes=[], dim=0)
x1 = torch.randn(32, 64, 8, 79) # 32 is the batch size; 64 is channel of output tensor; 8 is split size to be used; 79 is the size of other dimensions in both inputs and outputs.
