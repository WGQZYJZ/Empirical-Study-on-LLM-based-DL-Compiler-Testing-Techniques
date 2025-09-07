
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(dim_q, dim_k)
 
    def forward(self, qk, k, v):
        scaled_qk  = torch.matmul(qk, k.transpose(-2, -1)).div(inv_scale_factor) # Compute the dot product of a query and a key tensor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the output of the dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(v) # Compute the dot product of the dropout output and a value tensor
        return output


# Initializing the model
m = Model()
q = torch.randn(1, dim_k, seq_len, hid_dim // dim_k * num_heads).to('cuda')
k = torch.randn(1, dim_k, seq_len, hid_dim // dim_k * num_heads).to('cuda')
v = torch.randn(1, dim_v, seq_len, hid_dim // dim_v * num_heads).to('cuda')
