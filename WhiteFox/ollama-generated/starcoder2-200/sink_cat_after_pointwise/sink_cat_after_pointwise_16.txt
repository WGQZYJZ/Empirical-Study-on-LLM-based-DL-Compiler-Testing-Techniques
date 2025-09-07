
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        v1 = torch.cat([x1, y2], dim=...) # Concatenate 2 tensors along a dimension.
        v2 = v1.view(-1) # Reshape the concatenated tensor to one dimension.
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 50) # A dummy 3rd input of shape (2, 50).
y2 = torch.randn(87, 49) # Another dummy 3rd input of shape (87, 49).

