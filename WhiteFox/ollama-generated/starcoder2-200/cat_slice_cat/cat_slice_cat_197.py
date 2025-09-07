
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensors):
        v1 = torch.cat(input_tensors, dim=1)
        size = 9223372036854775807 # Size of the slice along dimension 1 
        v2 = v1[:, 0:size]
        v3 = v2[:, 0:size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4


# Initializing the model