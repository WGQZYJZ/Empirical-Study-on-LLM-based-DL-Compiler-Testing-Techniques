
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], dim=0)
        v  = v.view(-1, ) # view the concatenated tensor as a vector instead of a matrix
        v = torch.relu(v)

        return v

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(32, 64)
x2  = torch.randn(32, 64)

