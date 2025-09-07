
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()
 
    def forward(self, input_tensors):
        v1 = torch.cat(input_tensors, dim=1)
        v2  = v1[:, :size]
        v3  = v1[:, size:] # Slicing the concatenated tensor along dimension 1
        v4  = torch.cat([v1, v2], dim=1)
        return v4


# Initializing the model
m  = Model(50)


# Inputs to the model
x1_ = torch.randn(3, 976, 848)
x2_ = torch.randn(3, size - 976, 848) # Slices input tensors along dimension 1 in different sizes from 50 to 976 and 976 to the max of the sizes present in the concatenated tensor


x1  = torch.tensor([[
    [
        [-2.343244e-03,  8.386609e+01], 
        [-5.213369e+01,-7.802807e+02],
        ..., 8.226950e+00]
    ]
])


x2 = torch.tensor([
  [[-4.176613,  3.276034]]
])
__output__  = m( [ x1_, x2_ ])

