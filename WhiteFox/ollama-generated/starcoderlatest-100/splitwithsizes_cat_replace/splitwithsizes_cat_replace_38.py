
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.split(x1, [5], dim=3) # Split the input tensor into several tensors along a given dimension
        v2 = torch.cat([v1[i] for i in range(len(v1))], dim=3) # Concatenate the split tensors along the same dimension
