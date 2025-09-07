
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
    def forward(self, input1, input2):
        split_tensors  = torch.split(input1, [5, 8], dim) 
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=dim)
        return concatenated_tensor


# Initializing the model with dim of 0
m0 = Model()
 
x1  = torch.randn(3, 4, 6)
x2  = torch.randn(3, 5, 8)
# Inputs to m0 and m1 are (x1, x2) = ([x1_split[0], x1_split[1]], [x2])
__output__m0 = m0(x1, x2)
 
# Initializing the model with dim of 1
m1 = Model(dim=1)
 
x1  = torch.randn(3, 4, 5)
x2  = torch.randn(3, 8, 6)
__output__m1 = m1(x1, x2)

