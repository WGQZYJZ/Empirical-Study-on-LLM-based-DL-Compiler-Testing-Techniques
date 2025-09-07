
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], 0)
        v2 = v1.view(-1) # Reshape the concatenated tensor 
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model(dim=...)

# Inputs to the model
x1, x2  = torch.randn(batch_size,...), torch.randn(batch_size, ...) # The tensors of the same dimensionality


