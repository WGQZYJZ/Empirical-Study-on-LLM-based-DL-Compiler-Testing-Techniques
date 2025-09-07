
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value, inv_scale=None):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output
# Initializing the model
scaled_dot_product = ScaledDotProductAttention()


def forward():
    # Inputs to the model
    query = torch.randn(1, 3, 64, 64)
    key   = torch.randn(8, 3, 64, 64)
    value = torch.randn(8, 3, 64, 64)

    # Computing the attention weights and then using them to compute a weighted sum of values
    output  = scaled_dot_product(query, key, value, inv_scale=torch.sqrt(key.size(-1)))
    return output

def test():
    # Inputs to the model
    query = torch.randn(1, 3, 64, 64)
    key   = torch.randn(8, 3, 64, 64)
    value = torch.randn(8, 3, 64, 64)

    # Computing the attention weights and then using them to compute a weighted sum of values
    scaled_dot_product(query, key, value, inv_scale=torch.sqrt(key.size(-1)))
# Please generate a valid PyTorch model example with public PyTorch APIs meets the specified requirements. Plus, please also generate the input tensor for the newly generated model.

