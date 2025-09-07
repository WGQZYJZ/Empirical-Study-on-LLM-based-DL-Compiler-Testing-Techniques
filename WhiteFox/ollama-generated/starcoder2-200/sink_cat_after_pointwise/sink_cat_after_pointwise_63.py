
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.cat([x1[0], x1[1]], dim=0)
        t2  = v.view(-1, 4).reshape(8, -1) # Reshape the concatenated tensor after a concatenation operation
        return torch.nn.functional.relu(t2)


# Initializing the model
m  = Model()

# Inputs to the model
x1  = [torch.randn(4), torch.randn(3, 5)] # Two tensors. First one is of shape (4,) and second one is of shape (3, 5).


