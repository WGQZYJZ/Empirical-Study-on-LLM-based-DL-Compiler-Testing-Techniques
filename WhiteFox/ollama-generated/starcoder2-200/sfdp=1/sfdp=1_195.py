
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, q1, k1, v1):
        v2  = torch.matmul(q1, k1.transpose(-2, -1)) # Compute the dot product of the query and key tensors.
        v3  = v2 / math.sqrt(k1.size(-1))         # Scale the dot product by 1/√N (number of channels).
        v4  = torch.nn.functional.softmax(v3, dim=-1)  # Apply softmax to the scaled dot product.
        v5  = torch.nn.functional.dropout(v4, p=0.2)   # Apply dropout with probability 0.2.
        v6  = v5.matmul(v1)                       # Compute the dot product of the dropout output and value tensor.
        return v6

# Initializing the model
m  = Model()

