
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
        self.weight1 = torch.randn(dim * 3)
        self.weight2 = torch.randn(dim ** 4)

    def forward(self, x0):
        t1 = torch.cat([x0, self.weight1], -1) # Concatenate two tensors along the final dimension
        t2 = t1[..., :dim] # Grab a specific slice of that reshaped tensor and store it in another tensor
        t3 = self.weight2[None].expand_as(t2) + torch.relu(t2 * 2.) # Apply ReLU to the reshaped tensor, and then multiply with an scalar parameter, then add this result back.
        return t3


# Initializing the model
m = Model()

# Inputs to the model