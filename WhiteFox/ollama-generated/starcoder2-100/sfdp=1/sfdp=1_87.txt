
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.matmul(x1[0], x1[1].transpose(-2, -1))  # Compute the dot product of the query and key tensors
        v3 = v2 / 64
        v5 = v3.softmax(dim=-1)  # Apply softmax to the scaled dot product
        return torch.nn.functional.dropout(v5, p=0.7), x1[0], x1[1]


# Initializing the model
m  = Model()
 
# Inputs to the model
q  = (torch.randn(32, 64),
      torch.randn(32, 32))
