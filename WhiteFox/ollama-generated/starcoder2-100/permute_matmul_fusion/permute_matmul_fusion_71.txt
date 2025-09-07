
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.bmm(x1.permute(-1,-2), x2) # or torch.matmul(x1.permute(-1,-2), x2) for the 3-D bmm
        return v1

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(5,48000) # size of the input A is [batch_size, dim] or [batch_size, dim, 1], etc.
x2  = torch.randn(3*7, 3*9) # size of the input B is [batch_size, dim, 1].
__output__   = m(x1, x2)

