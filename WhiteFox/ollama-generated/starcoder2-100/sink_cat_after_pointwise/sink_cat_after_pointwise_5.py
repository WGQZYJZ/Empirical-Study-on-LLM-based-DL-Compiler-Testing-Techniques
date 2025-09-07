
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=...)  # Concatenate tensors along a dimension
        t2 = t1.view(-1, ...)  # Reshape the concatenated tensor
        t3 = t3 = t2.relu() 
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(20)
x2 = torch.randn(1, 20)

