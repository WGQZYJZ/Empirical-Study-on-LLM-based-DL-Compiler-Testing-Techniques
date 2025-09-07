
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, 4096, dim=3) # split the input tensor into several tensors with size (B, C/2, H, W) along the channel dimension.
        v2 = torch.cat([v1[i] for i in range(len(v1))], dim=3) # Concatenate these split tensors back to one with the same size of input tensor.
        return v2

# Initializing the model