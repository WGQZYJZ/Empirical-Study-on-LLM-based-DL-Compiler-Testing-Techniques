
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v  = torch.split(x1, [8], dim=2) # Split the input tensor along dimension 0 with split sizes of size 4 and length 3; the split tensors are stored in a tuple
        return torch.cat([v[i] for i in range(len(v))], dim=2)
 
# Initializing the model
m = Model()
 
# Input to the model: torch.randn(1, 4, 8). This input tensor is split into three tensors with size 3 and dimension 0; this information can be obtained using `torch.split`. This is used for testing the `is_valid_splitwithsizes_cat` optimization.
x = torch.randn(1, 4, 8)

