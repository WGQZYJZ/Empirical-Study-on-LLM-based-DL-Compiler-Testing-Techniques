
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, size):
        v1 = torch.cat([x1[0], x1[-1]]) # Concatenate input tensors along dimension 1
        v2 = v1[:, :size] # Slice the concatenated tensor along dimension 1
        return torch.cat([v1, v2], dim=1) # Concatenate original and sliced tensors


# Initializing the model