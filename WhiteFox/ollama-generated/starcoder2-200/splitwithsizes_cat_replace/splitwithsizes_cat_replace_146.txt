
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.split(x1, [50], dim=3) # Split the input tensor into two tensors with lengths of 50 along the third dimension. The third dimension is assumed to be the channel dimension.
        v2_tensorlist = []
        for v1i in range(len(v1)):
            v2i = torch.cat([torch.full((2,4), fill_value=v1[v1i], device='cuda:0')], dim=3) # Concatenate a 3x4 tensor of zeros along the third dimension with each of the split tensors in the list. The third dimension is assumed to be the channel dimension.
            v2_tensorlist.append(v2i)
        v2 = torch.stack(v2_tensorlist, dim=0) # Stack these concatenation tensors into a 3x50-element tensor along the first dimension.
        return v1

# Initializing model
m = Model()

