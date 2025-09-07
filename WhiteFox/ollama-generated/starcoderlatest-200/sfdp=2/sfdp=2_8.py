
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk / scale_factor # Scale the dot product by the scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
query  = torch.randn(1, num_heads, input_dim) # [1, 8, 64]
key    = torch.randn(num_heads, num_heads, value_dim) # [8, 8, 512]
value  = torch.randn(num_heads, value_dim,   key.size(-2)) # [8, 512, 64]
