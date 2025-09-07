
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.split(x1, 32, dim=0) # Split the input tensor into tensors of size 32 along the first dimension using torch.split
        concatenated_tensor = torch.cat([v2[i] for i in range(len(v2))], dim=-1) # Concatenate these split tensors along the last dimension with torch.cat, and set the concatenation axis to -1 as it is typically used in PyTorch for 3D inputs
        return concatenated_tensor


# Initializing the model