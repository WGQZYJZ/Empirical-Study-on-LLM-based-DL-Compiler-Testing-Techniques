
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = x1.permute(...) # Permute the input tensor A
        t2 = x2.permute(...) # Permute the input tensor B
        v3 = torch.bmm(t1, t2) # or torch.matmul(t1, t2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(...)
x2 = torch.randn(...)
