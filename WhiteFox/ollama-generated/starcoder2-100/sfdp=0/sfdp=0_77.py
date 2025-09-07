
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=10e5) -> None:
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / (
                inv_scale ** 0.5)
        attention_weights = scaled_dot_product.softmax(dim=-1)
 
        output = attention_weights.matmul(value)
        return output
 
scaled_dot_product_attention = ScaledDotProductAttention()


# Initializing the model
m  = ScaledDotProductAttention()

# Inputs to the model
query = torch.randn([32, 16])
key = query * 0.5
value = key + 1

