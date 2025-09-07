
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_weight = torch.nn.Parameter(torch.zeros(3, 8, dtype=torch.float))

    def forward(self, query, key, value, attn_mask):
        # Computed as: scale_dot_product_attention = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)), 
        # where the scaling is done by dividing by sqrt(d_k), so that q and k are unit vectors.
        # Then, add the attention mask to the scaled dot product
        scale_dot_product_attention = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        scale_dot_product_attention = scale_dot_product_attention + attn_mask

        # Then apply softmax on the result of scaled dot product attention to obtain the attention weights, 
        # and multiply the attention weight by the corresponding value tensor to get the final output.
        attn_weight = torch.softmax(scale_dot_product_attention, dim=-1)
        output = attn_weight @ value

        return output


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
key = torch.randn(8, 3, 64, 64)
value = torch.randn(8, 3, 64, 64)
attn_mask = torch.randn(1, 1, 64, 64)
