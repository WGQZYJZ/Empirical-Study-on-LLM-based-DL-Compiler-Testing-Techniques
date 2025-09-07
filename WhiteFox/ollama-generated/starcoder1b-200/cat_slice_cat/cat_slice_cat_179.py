
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)  # Concatenate the two input tensors along dimension 1
        v2 = v1[:, 0:9223372036854775807]  # Slice the concatenated tensor along dimension 1
        v3 = torch.cat([v1, v2], dim=1)  # Concatenate the two slices of the original concatenated tensor along dimension 1
        return v3


# Initializing the model
m = Model()
