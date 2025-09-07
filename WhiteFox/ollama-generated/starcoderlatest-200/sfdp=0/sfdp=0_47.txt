
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    # No additional modules needed for this model
 
    def forward(self, query, key, value, inv_scale=None):
        # Apply scaled dot product attention to the input tensor (i.e., a 2-D tensor with shape `(batch size x sequence length x embedding dimension)`, where batch size is equal to that of the input tensors in `query`, `key` and `value`). Here is an example implementation of the Scaled Dot-Product Attention mechanism. Please use the PyTorch documentation for your reference, which can be found [here](https://pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html).
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = ScaledDotProductAttention()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
query = torch.randn(1, 8, 64, 64)
key = torch.randn(1, 8, 64, 64)
value = torch.randn(1, 8, 64, 64)
inv_scale = x1.shape[-1] ** -0.5
