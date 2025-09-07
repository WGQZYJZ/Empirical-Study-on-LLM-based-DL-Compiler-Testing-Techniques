
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, key, value, dropout_p=0.5, inv_scale_factor=3):
        v1  = torch.matmul(x1, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        v2  = v1 / inv_scale_factor  # Scale the dot product by the inverse scale factor
        v3  = v2.softmax(dim=-1)  # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)  # Apply dropout to the softmax output
        v5  = value.matmul(v4)  # Compute the dot product of the dropout output and the value
        return v5


# Initializing the model
m = Model()

# Input tensors
key  = torch.randn(1, 3072, 8, 64)
value  = torch.randn(1, 8, 96, 38)
x1  = torch.randn(1, 8, 96, 38)

# Model execution and results
__output__  = m(x1, key=key, value=value)