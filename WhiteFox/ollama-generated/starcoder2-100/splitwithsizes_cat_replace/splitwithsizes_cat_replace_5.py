
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        splitted  = torch.split(x1, [8], dim=2) # Split the input tensor along dimension 3 into two tensors of size (N, 64, 8).
        concatted_tensor  = torch.cat([splitted[0], splitted[1]], dim=2) # Concatenate these two tensors back to a single tensor.
        return concatted_tensor

# Initializing the model