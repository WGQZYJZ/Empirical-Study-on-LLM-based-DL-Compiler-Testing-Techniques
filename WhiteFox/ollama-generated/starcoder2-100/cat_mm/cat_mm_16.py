
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Matrix multiplication of two input tensors
        v2 = torch.cat([v1] * self.dim, dim)  # Concatenation of the result tensor along a specified dimension
        return v2


# Initializing the model
m = Model()
dim_to_concat = 0
 
input1 = torch.randn(32, 64)
input2 = torch.randn(64, 128)
