
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1) # Concatenate the two tensors along dimension 1
        v2 = v1[:, :9223372036854775807] # Slice tensor 1 along dimension 1
        v3 = v2[:, :32]           # Further slice tensor 1 along dimension 1
        return torch.cat([v1, v3], dim=1)   # Concatenate the concatenated tensor and sliced tensor along dimension 1


# Initializing the model
m = Model()

