
class ScaledDotProductAttention(nn.Module):
    def __init__(self, config: Any = None) -> None:
        super().__init__()

        self.dropout  = nn.Dropout(config.attention["attention_probs_dropout_prob"])
 
    def forward(self, query, key, value):
        scaling  = (key[0].shape[-1]) ** (-0.5) # sqrt(dimension of the key/query vector)
        scaled_dot_product  = torch.matmul(
            query / scaling, 
            key.transpose(-2, -1))
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights * value
 
        return output


# Initializing the model
m  = ScaledDotProductAttention()

# Inputs to the model
query  = torch.randn(32, 640, 768)
key  = torch.randn(1954304, 768)
value  = torch.randn(1954304, 1024)


__output__  = m(query, key, value)