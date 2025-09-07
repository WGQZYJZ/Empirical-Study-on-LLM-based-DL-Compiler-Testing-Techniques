
class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output


# Initializing the model
m = SelfAttention()


# Inputs to the model
q1 = torch.randn(1, 3, 64, 64)
k1 = torch.randn(1, 8, 64, 64)
v1 = torch.randn(1, 8, 64, 64)


# Forward pass of the model
out1 = m(q1, k1, v1)


