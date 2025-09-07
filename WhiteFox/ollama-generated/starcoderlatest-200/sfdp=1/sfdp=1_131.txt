
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim, num_heads)
 
    def forward(self, query, key, value, scale_factor=None):
        v = torch.matmul(query, self.k_mat).transpose(-2, -1)  # Compute the dot product of the query and the key tensor
        scaled_v = v.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_v = scaled_v.softmax(dim=-1)  # Apply softmax to the scaled dot product
        output = torch.matmul(softmax_v, value).transpose(-2, -1)  # Compute the dot product of the attention output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(3, embed_dim, head_num, sequence_length)
key   = torch.randn(embed_dim, head_num, sequence_length)
value = torch.randn(head_num, embed_dim, sequence_length)
