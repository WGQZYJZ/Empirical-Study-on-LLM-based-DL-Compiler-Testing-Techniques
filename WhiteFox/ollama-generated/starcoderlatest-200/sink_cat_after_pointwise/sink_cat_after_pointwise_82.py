
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1) # Concatenate x1 and x2 along dimension 1
        t2 = t1.view([-1, 3])           # Reshape concatenated tensor to shape [n, 3]
        t3 = self.relu(t2)               # Apply pointwise unary operation ReLU on the reshaped tensor
        return t3


# Initializing the model
m = Model()

x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 3, 2)
