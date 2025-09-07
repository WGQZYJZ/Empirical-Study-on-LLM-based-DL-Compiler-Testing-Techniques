
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(num_heads=4, input_dim=60793, output_dim=512)
 
    def forward(self, x1, query, key, value):
        qk  = self.attention(x1, query, key, attn_mask=None,
                            need_weights=False, need_head_weights=False)[0]
        scaled_qk  = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output     = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 60793, 15, 15)
query  = torch.randn(4, 32768, 15, 15) # The length of query must be equal or less than num_heads * hidden_dim / head_dim!
key     = torch.randn(8, 32768, 15, 15)
value   = torch.randn(4, 60793, 15, 15) # The length of value must be equal or less than num_heads * hidden_dim / head_dim!
