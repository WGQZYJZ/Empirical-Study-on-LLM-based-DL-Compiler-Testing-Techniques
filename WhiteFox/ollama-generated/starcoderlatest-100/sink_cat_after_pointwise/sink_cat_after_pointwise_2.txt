
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=1) # concatenated tensor of dimension 3, [x1, x1] => [[x1, x1], [x1, x1]]
        v2 = v1.view((v1.size(0), -1))
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 6, 2)
