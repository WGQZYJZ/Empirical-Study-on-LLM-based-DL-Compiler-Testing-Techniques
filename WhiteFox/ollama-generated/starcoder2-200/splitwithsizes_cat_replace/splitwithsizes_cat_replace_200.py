
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.split(x1, 32, dim=1) # Split the input tensor into several tensors along dimension 1 using size 32
        v1 = torch.cat([v[0] for v in v0],dim=1) # Concatenate these split tensors along the same dimension and reorder them according to their original order (i.e., concat_split_tensors = [split_tensors[i] for i in range(len(split_sizes))])
        return v1
# Initializing the model