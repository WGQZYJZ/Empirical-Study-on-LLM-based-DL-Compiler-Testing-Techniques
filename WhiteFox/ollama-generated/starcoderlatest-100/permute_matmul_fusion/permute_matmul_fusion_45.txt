
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=-1) # Permute the input tensor
        v2 = torch.bmm(v1, v1.permute(-2, -1)) # or torch.matmul(v1, v1.transpose(-2, -1))
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 5)
x2 = torch.randn(1, 3)
