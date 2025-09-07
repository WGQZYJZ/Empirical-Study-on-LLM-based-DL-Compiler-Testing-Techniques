
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=-1) # Concatenate tensors along the -1th dimension
        v2 = v1.view(-1, 8) # Reshape concatenated tensor
        v3 = torch.nn.functional.relu(v2) # Pointwise activation
        return self.linear(v3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4)
x2 = torch.randn(1, 2)
