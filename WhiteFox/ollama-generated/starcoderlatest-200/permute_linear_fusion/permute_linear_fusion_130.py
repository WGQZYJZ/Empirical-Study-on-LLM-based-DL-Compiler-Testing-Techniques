
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.unsqueeze(x1, 0) # Broadcast the dimension of input_tensor to 4D
        v2 = torch.permute(v1, (0, 3, 2, 1)) # Permutation operation that swaps the last two dimensions of a tensor with more than two dimensions
        v3 = torch.squeeze(v2) # The number of dimensions should be reduced to 2 after squeezing.
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 3, 5)
