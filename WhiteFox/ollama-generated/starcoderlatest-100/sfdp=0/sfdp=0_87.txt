
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    # The scaled dot product attention layer takes in two tensors, query and value, and computes a weighted sum of them.
    # Query: [batch_size, num_heads, q_len, d_model/num_heads]
    # Key: [batch_size, num_heads, k_len, d_model/num_heads]
    # Value: [batch_size, num_heads, v_len, d_model/num_heads]
    def forward(self, query, key, value):
        # Calculate the dot product between the queries and keys using PyTorch's addmm function.
        scaled_dot_product = torch.addmm(dim=1, alpha=inv_scale, beta=0.0, mat1=query, mat2=key.transpose(-2, -1))
 
        attention_weights = F.softmax(scaled_dot_product, dim=-1)  # The softmax function has been implemented for you
        # Now apply a weighted sum of the values across the heads to get the output.
        output = torch.matmul(attention_weights, value)

        return output


# Initializing the model
model2 = ScaledDotProductAttention()
# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key = torch.randn(1, 8, 64, 64)
value = torch.randn(1, 8, 64, 64)
