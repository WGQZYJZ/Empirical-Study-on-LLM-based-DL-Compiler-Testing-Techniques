
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of a query and a key
        scaled_qk  = qk.div(scale)                       # Scale the dot product by an inverse scale factor 
        softmax_qk  = scaled_qk.softmax(dim=-1)           # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        out = dropout_qk.matmul(value)                    # Compute the dot product of the dropout output and a value 
        return out


# Initializing the model
m  = Model()

# Inputs to the model
q1, k1, v1  = torch.randn(16, 256), torch.randn(4096, 256), torch.randn(384, 4096)

