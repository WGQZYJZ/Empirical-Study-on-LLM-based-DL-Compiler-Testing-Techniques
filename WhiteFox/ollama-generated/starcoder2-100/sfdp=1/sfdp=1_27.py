
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.matmul(x1)  # Compute the dot product of a query and key tensor
        v1 = v0 / inv_scale_factor
        v2 = v1.softmax(dim=-1)
        return v3


# Initializing the model
m  = Model()
 
# Input to the model
x1 = torch.randn(8, 5, 4)

__output__  = m(x1)
