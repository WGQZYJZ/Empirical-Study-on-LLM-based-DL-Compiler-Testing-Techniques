
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 3)

    def forward(self, x1):
        v1 = torch.cat([x1.permute(0, 2, 1), x1], dim=1) # Permute the input tensor to form the linear transformation of two vectors.
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 3)
