
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=-1):
        super().__init__()
        self.dim = dim
        self.scale = 0.05

    def forward(self, x1, x2, mask):
        # The scaled dot product of queries with keys gives the raw attention scores. 
        # We compute the softmax over these scores to get an attention score per token.
        x1_dot_x2 = torch.matmul(x1, x2.transpose(-2, -1)) / self.scale

        # Apply a mask of 0 for padding tokens. This is useful when the input tensor has zero values, such as self-attention for a pre-trained Transformer model or linear layer in an AutoEncoder.
        attention_weights = torch.exp(x1_dot_x2 * -1e10) * mask

        # Normalize over the attention scores to get probabilities.
        attention_weights = attention_weights / torch.sum(attention_weights, dim=-1).unsqueeze(-1)
        return attention_weights


# Initializing the model
m = ScaledDotProductAttention()


