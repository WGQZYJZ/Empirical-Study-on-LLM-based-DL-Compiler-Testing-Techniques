
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, v1):
        v2 = torch.matmul(v1, v3)  # Compute the dot product of the query and key
        v4 = torch.softmax(v5 + v6, dim=-1)  # Apply softmax to the scaled dot product (additive dropout)
        return v7


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(32, 198, 50)
__output__  = m(x1)

