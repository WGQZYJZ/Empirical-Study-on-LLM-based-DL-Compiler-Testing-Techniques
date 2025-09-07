
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1)  # Concatenate along dimension 1
        t2 = t1.view(-1, 4) # Reshape tensor with shape (-1, 4)
        return torch.relu(t2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 2)
x2 = torch.randn(6, 2)
