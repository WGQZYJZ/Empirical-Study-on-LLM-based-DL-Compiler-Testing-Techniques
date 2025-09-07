
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=-1)
        v2 = v1.view(v1.size(0), -1)  # Reshape the concatenated tensor with (-1,2) as the last dimension size to use torch.nn.functional.relu
        return self.relu(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
x2 = torch.randn(1, 5)
