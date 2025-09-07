
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.split(x1, [3], dim=0) # Split the input tensor into three tensors along dimension 0 with size 3 in each split, and the third split tensor has a size of 5 
        concatenated_tensor = torch.cat([v2[i] for i in range(len(split_sizes))], dim=1)
        return concatenated_tensor


# Initializing the model
m = Model()
x1 = torch.randn(8, 3, 64, 64) # The input tensor is a 3D tensor with shape (8 x 3 x 64 x 64).

__output__  = m(x1)

