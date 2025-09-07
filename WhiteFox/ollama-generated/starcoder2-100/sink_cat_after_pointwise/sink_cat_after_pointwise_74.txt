
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], 0) # Concatenate tensors along a dimension.
        v2 = v1.view(-1, ) # Reshape the concatenated tensor to have a single dim.
        v3 = torch.relu(v2) # Apply ReLU unary operation on the reshaped tensor.
        return v3

# Initializing the model
m  = Model()

