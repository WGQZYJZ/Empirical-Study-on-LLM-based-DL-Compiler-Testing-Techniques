
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1):
        v  = torch.cat([t1, t2], dim=0) # Concatenate tensors along the first dimension.
        v2 = v.view(-1)                  # Reshape to a vector with the original size.
        v3 = F.relu(v2)                   # Apply ReLU pointwise.
        return v3

# Initializing model
m  = Model()

# Input tensors
t1  = torch.randn(4, 8000)
t2  = torch.randn(4, 9000)

