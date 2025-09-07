
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value): 
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of a query tensor and a key tensor.
        v2  = v1 / inv_scale_factor # Scale the dot product by an inverse scale factor.
        v3  = scaled_qk .softmax(dim=-1) # Apply softmax to the scaled dot product.
        v4  = torch.nn.functional.dropout(v3, p=dropout_p) # Apply dropout to the softmax output.
        v5  = v2 * value # Compute the dot product of the dropout output and a value tensor.
        return v6

# Initializing the model
m = Model()

