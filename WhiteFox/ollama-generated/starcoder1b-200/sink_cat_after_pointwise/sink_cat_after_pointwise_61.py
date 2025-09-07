
class Model(torch.nn.Module):
    def __init__(self, hidden_dim=32):
        super().__init__()
        self.layer1 = torch.nn.Linear(2, hidden_dim)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Invert the tensor permutation: permute (channel dim, height dim, width dim), then reverse (height dim, width dim, channel dim).
        return self.layer1(v2)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 2, 2) # Original input tensor
x2  = torch.randn(1, 2, 3, 4) # Input tensor after swapping channels and height and width dimensions
