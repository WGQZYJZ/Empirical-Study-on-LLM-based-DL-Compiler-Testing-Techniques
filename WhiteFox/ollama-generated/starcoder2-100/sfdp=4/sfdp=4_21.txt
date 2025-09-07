
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value, attn_mask=None):
        qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(
            query.size(-1)
        )  # Scale the dot product of query and key using the square root of the size of the last dimension of each tensor
        if attn_mask is not None:
            qk = (
                qk + attn_mask
            )  # Add the attention mask to the scaled dot-product, which prevents the model from attending to certain positions in the input sequence.
        attn_weight = torch.softmax(qk, dim=-1)  # Compute the softmax of the scaled dot product to obtain the attention weights
        output = torch.matmul(attn_weight, value).contiguous()  # Calculate a weighted sum using the attention weights and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(64, 8, 2500)
key   = torch.randn(64, 192, 2500)
value = torch.randn(64, 32, 2500)
__output__  = m(query, key, value)

