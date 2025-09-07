
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute(...).contiguous()
        v3  = torch.bmm(v1, x2) # or v4 = torch.matmul(v1, x2) for PyTorch 1.6 or above
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(10, 50)
x2 = torch.randn(10, 49, 70)
