
class Model(torch.nn.Module):
    def __init__(self, attention_dim, num_heads):
        super().__init__()
        self.attention_layer = torch.nn.MultiheadAttention(embed_dim=attention_dim, num_heads=num_heads)
 
    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk  = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)   # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output  = self.attention_layer(query=dropout_qk, key=value, value=None)[0] # Compute the attention mechanism of the query with all available keys
        return output


# Inputs to the model
x1 = torch.randn(2, 8, 64, 64)
