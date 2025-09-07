
class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    # Input shape: (batch_size, num_heads, head_dim)
    # Attention weights shape: (batch_size, num_heads, query_len, key_len)
    def forward(self, qk):
        scaled_dot_product = torch.matmul(qk[0], qk[1].transpose(-2, -1)) / math.sqrt(qk[0][:, 0, :].shape[-1]) # In this code, the number of heads are always equal to 8 for simplicity
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(qk[2])

        return output


# Initializing the model
a = SelfAttention()

# Inputs to the model
input_x1 = torch.randn((1, 8, 64, 64))
