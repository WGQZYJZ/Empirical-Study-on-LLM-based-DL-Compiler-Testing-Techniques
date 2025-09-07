
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, config: PretrainedModelConfig):
        super().__init__()
 
        self.scale = 1 / math.sqrt(config.attention_head)
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) * self.scale

        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output


# Initializing the model
scaled_dot_product_attention  = ScaledDotProductAttention()
 
 
