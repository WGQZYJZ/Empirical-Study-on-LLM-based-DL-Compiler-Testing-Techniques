
class Model(torch.nn.Module):
    def __init__(self, num_head):
        super().__init__()
        self.num_head = num_head
        self.attn1 = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)
 
    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        attn2_output = self.attn1(query, key, value=None, attn_mask=None)[0] # Compute the attention score matrix of the query with all keys (including itself), where each element is divided by sqrt(attention head dimension)
        return attn2_output


# Initializing the model
m = Model(num_head=8)


# Inputs to the model
query  = torch.randn(1, 3, 64, 64)
key  = torch.randn(2, 8, 64, 64)
