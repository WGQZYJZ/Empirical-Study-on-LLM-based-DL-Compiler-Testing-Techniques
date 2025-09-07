
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)  # Concatenate input tensors along a dimension of index 1
        v2 = v1.view(v1.size(0), -1)  # Reshape the concatenated tensor into (-1,), and we want to reduce the tensor size by 1
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()


