
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(dim_q, dim_k)
 
    def forward(self, x1, x2):
        v1 = torch.matmul(x1, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk  = v1.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        v2 = self.attention(dropout_qk).matmul(value) # Compute the dot product of the dropout output and the value tensor
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, dim_q, seq_len, embed_dim)
x2 = torch.randn(seq_len, dim_k, dim_v)
