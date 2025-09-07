
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)  # Concatenate the input tensors along dimension 1
        v2 = v1[:, 0:9223372036854775807]  # Slice the concatenated tensor along dimension 1
        v3 = v2[:, 0:9223372036854775807]  # Further slice the tensor along dimension 1
        return torch.cat([v1, v3], dim=1)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(2, 3, 64, 64)
x2  = torch.randn(2, 3, 64, 64)
