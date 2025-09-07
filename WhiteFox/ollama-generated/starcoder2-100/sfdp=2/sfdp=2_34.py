
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale_factor=2000000000., dropout_p=0.1):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk / inv_scale_factor   # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)    # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)        # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model()
 
# Inputs to the model
query  = torch.randn(4, 60, 2512)
key   = torch.randn(4, 3792, 2512)
value = torch.randn(4, 288, 512)
 
__output__  = m(query, key, value)

