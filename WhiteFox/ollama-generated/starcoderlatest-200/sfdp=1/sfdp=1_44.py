
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=10, num_heads=2)
 
    def forward(self, q, k, v):
        attn_output = self.attn(q, k, v)[0]
        scaled_attn_output = attn_output.div(inv_scale_factor)
        softmax_attn_output = scaled_attn_output.softmax(dim=-1)
        dropout_attn_output = torch.nn.functional.dropout(softmax_attn_output, p=dropout_p)
        output = dropout_attn_output.matmul(v)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(1024, 128, 56, 56)
k = torch.randn(1024, 128, 56, 56)
v = torch.randn(1024, 128, 14, 14)
