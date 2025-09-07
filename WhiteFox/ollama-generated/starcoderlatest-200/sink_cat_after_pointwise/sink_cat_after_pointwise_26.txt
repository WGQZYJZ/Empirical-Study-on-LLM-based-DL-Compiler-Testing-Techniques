
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0) # concat along 0-th axis
        v2 = v1.view(-1, 4) # reshape v1
        v3 = torch.nn.functional.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 5, 2)
x2 = torch.randn(4, 6, 2)
