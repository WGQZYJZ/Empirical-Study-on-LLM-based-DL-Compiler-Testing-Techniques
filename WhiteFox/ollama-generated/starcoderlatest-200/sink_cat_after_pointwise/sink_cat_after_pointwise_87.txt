
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=2) # Permute the input tensor in 3 dimensions (dim=2 here means second last dimension)
        t2 = t1.view(-1, 4)
        return torch.relu(t2)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(20, 2, 2)
x2 = torch.randn(5, 2, 2)
