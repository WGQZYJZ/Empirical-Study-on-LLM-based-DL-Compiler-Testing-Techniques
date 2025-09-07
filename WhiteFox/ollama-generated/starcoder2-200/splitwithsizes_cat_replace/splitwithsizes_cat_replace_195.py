
class Model(torch.nn.Module):
    def __init__(self, split_sizes):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.split(x1, [8], dim=3) # Split the input tensor into two tensors along dimension 3. The first tensor has size (B, 4*32, H, W), and the second one is of shape (B, 4*32, H, split_sizes[0])
        v1 = torch.cat([v1[0], v1[-1]], dim=3) # Concatenate the two tensors along dimension 3 using torch.cat to form a single tensor with shape (B, 4*32, H, W)
        return v1


# Initializing the model