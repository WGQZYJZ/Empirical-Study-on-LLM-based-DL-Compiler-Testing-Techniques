
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): # Input tensor 1
        v2 = torch.relu(x1) # Apply ReLU to input tensor 1 directly
        t1 = [v2, v3] # Concatenate two tensors with no user before sinking
        v4 = torch.cat(t1, dim=0).view(-1, 4) # Reshape the concatenation of two tensors as (-1, 4)
        return v4

# Initializing model and inputs to it
m = Model()

x1 = [
    np.array([23, -987]), # A tensor that concatenates the result of an arithmetic operation with a constant
    np.array([-0, 3]), # Another one
]


