
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0) # Concatenate inputs along the channel dimension
        t2 = t1.view(-1, 4) # Reshape the concatenated tensor to a 2D matrix of (4, D) shape where D is the length of input1 + input2
        v3 = torch.nn.functional.relu(t2) # Apply pointwise ReLU operation to reshaped tensor
        return v3

# Initializing the model
m = Model()


# Inputs to the model, 5x2 tensors
x1 = torch.randn(5, 2, 2)
x2 = torch.randn(5, 2, 2)
