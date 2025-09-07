
class AttentionModel(torch.nn.Module):
    def __init__(self, dim_head: int, num_heads: int):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(dim_key=dim_key, dim_value=dim_value, num_heads=num_heads)
 
    def forward(self, x1, x2, query):
        # Forward pass for MultiheadAttention is the same as that for a single head attention
        qk = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = AttentionModel()
 
# Inputs to the model
query = torch.randn(1, dim_key, batch_size, length_q)
key = torch.randn(2, dim_key, batch_size, length_k)
value = torch.randn(2, dim_value, batch_size, length_v)
 
