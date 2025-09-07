
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, x1, x2, inv_scale=8.0):
        q1 = x1.transpose(-2, -1)  # (batch_size, heads, length_q, dim_key)
        v1 = x2.transpose(-2, -1)  # (batch_size, heads, length_v, dim_value)
        scaled_dot_product = torch.matmul(q1, v1) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v1)  # (batch_size, heads, length_q, dim_value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(16, 8, 32, 32).cuda()
x2 = torch.randn(16, 8, 1024, 512).cuda()
