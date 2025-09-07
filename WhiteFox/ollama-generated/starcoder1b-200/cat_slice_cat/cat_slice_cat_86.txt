
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1) # Concatenate the two tensors along dimension 1
        v2 = v1[:, 0:9223372036854775807]  # Slice out the first half of the original concatenated tensor along dimension 1
        v3 = v2[:, 0:9223372036854775807]  # Further slice out the second half of the sliced tensor along dimension 1
        return torch.cat([v1, v3], dim=1)


# Initializing the model
m = Model()
