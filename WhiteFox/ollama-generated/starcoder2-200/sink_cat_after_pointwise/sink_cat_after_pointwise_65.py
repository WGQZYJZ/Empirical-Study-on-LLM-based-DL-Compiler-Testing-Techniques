
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v  = torch.cat([x1, x2], dim=0) # concatenate two input tensors along the first dimension (dim-0).
        v2 = v.view(-1)                   # reshape this concatenated tensor to a 1d vector of size -1.
        v3 = torch.relu(v2)               # apply ReLU unary operator on the reshaped 1d vector.
        return v3


# Initializing model