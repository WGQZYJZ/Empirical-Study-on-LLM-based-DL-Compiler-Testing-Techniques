
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0) # Concatenate tensors along the first dimension
        v2 = v1.view(-1, 6) # Reshape the concatenated tensor. The shape should be (-1, 3).
        return self.linear(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3)
x2 = torch.randn(1, 4)
