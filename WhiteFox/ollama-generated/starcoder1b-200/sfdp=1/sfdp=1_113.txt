
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(d_model, 3 * d_k)
 
    def forward(self, x1, x2):
        q, k, v = m.qkv(x1), m.qkv(x2), m.value
        k = k.transpose(-2, -1).contiguous() # Unsqueeze the dimension of `k` to match the number of keys (in our case, batch size)
        v = v.transpose(-2, -1).contiguous() # Unsqueeze the dimension of `v` to match the number of values (in our case, query length x key length x values length)
        q = torch.nn.functional.linear(q, k)  # Compute the dot product of the query and key tensors
        scaled_qk = q.div(torch.sqrt(k.size(-1) + 1e-9)) # Scale the dot product by an inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return dropout_qk.matmul(v)  # Compute the dot product of the dropout output and the value tensor
