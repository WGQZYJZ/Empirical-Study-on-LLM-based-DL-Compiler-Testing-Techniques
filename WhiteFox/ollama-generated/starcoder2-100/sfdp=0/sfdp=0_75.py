class SDOT_Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query_, key_, value_, scale=0.5):
        scaled_dot_product  = torch.matmul(query_, key_.transpose(-2, -1)) / scale
        attention_weights = scaled_dot_product.softmax(dim=-1)

        # attention_weights = attention_weights.div(scale**0.5).add_(eps)
        output  = attention_weights .matmul(value_)

        return output

