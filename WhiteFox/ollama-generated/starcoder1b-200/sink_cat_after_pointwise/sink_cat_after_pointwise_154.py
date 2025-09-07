
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2, x3):
        v1  = x1.permute(0, 2, 1)
        v2  = torch.cat([v1, x3], dim=1) # Concatenate the input tensors along the first dimension
        v3  = self.linear(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(2, 2, 2)
x3 = torch.randn(2, 4, 6).permute(0, 2, 1)
