
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v3 = torch.relu(x1)

        v1  = torch.cat([v3], dim=0).view(-1,) # Concatenate tensors along a dimension. In this example, the dimension is set to 0.
        v2  = torch.cat([x1 + x2], dim=0).view(-1,)

        return v1, v2


# Initializing the model and inputs for the model