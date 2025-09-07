
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, qk, v):
        softmax_qk  = self.attention(qk, qk, v)[0]
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output      = dropout_qk.matmul(v)
        return output

# Inputs to the model
qk = torch.randn(1, head_size, query.shape[0], key.shape[1]) # Compute the dot product of the query and the key
scaled_qk  = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
output      = self.attention(qk, qk, v)[0] # Compute the dot product of the dropout output and the value
__output__  = output

