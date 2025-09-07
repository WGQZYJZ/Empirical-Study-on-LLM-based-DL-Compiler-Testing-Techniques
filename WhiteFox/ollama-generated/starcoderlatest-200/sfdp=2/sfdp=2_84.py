
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_key):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return (query * softmax_qk + query * dropout_qk)
 
    def __repr__(self):
        return 'SelfAttention({}, {})'.format(query, key)


# Initializing the model
m = Model()


# Inputs to the model
query_key = torch.randn(1, 3, 64, 64)
