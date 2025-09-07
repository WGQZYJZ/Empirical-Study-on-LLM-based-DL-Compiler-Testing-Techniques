
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2, x3], dim=0)  # Concatenate the input tensors along dimension 0 (along batch axis). 
        v2 = v1.view(v1.shape[0] * v1.shape[1], -1)  # Reshape the concatenated tensor
        return torch.relu(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 5, 7)
x2 = torch.randn(4, 6, 8)
x3 = torch.randn(5, 7, 9)
