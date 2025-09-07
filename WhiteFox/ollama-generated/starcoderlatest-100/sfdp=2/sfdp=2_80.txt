
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_linear = torch.nn.Linear(2048, 16384)
 
    def forward(self, query, key, value):
        v1 = self.attention_linear(query).permute(0, 2, 3, 1) # (b, n, d_k, h) -> (b, h, n, d_k)
        v2 = torch.nn.functional.normalize(v1, p=2, dim=-1) 
        v3 = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk  = v3.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
        return v2, v3, v4, v5


# Input to the model
query  = torch.randn(1, 60, 8, 8) # (batch_size=1, n_head, d_k, d_v) -> (1 x d_model x input_length x num_heads)
key    = torch.randn(1, 60, 8, 8) # (b, n_head, n_key, d_k) -> (1 x d_model x input_length x num_heads)
value  = torch.randn(1, 60, 12, 12) #(batch_size=1, n_head, n_key, d_v) -> (1 x d_model x input_length x num_heads)
 
# Expected output
# (b, d_k, h, n), (b, n_key, h, d_k), (b, n_key, d_k, h), (b, n_key, h, d_k)  -> (1 x input_length x batch_size x num_heads)
__output__, __output__, __output__, 