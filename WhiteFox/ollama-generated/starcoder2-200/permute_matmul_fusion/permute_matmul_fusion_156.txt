
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1)
        v2  = torch.bmm(v1, x2) # or torch.matmul(v1, x2)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(20, 35, 75)  # random input tensor A
x2  = torch.randn(35, 75)      # random input tensor B
__output__  = m(x1, x2)

