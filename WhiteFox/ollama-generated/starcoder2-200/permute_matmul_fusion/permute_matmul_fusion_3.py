
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute((0, 2, 1)) # Permute the first input tensor.
        v2 = torch.bmm(v1, x2)      # or torch.matmul(v1, x2). 
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(3, 4, 6)
x2 = torch.randn(3, 5, 7)
