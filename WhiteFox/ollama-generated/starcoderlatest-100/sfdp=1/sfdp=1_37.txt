
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        qk  = torch.matmul(q1, k1.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk  = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(v1) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()
 
# Query Tensor shape: [batch_size, query_length, num_head, d_k]
q  = torch.randn(8, 128, 64, 32) # [batch_size, query_length, key_length, num_heads, d_k]
 
# Key Tensor shape: [batch_size, key_length, num_head, d_v]
k  = torch.randn(8, 128, 64, 32) # [batch_size, query_length, key_length, num_heads, d_v]
 
# Value Tensor shape: [batch_size, value_length, num_head, d_v]
v  = torch.randn(8, 128, 64, 32) # [batch_size, query_length, key_length, num_heads, d_v]
 
