
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.Linear(in_features=28*28, out_features=50) # Apply a linear transformation to the input tensor
        v2  = torch.nn.ReLU()
        return v2(v1(x1))


# Initializing the model