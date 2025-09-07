
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, scale=1e-6, attn_dropout=0.5):
        super().__init__()
        self.scale = torch.tensor(scale)
        self.softmax = nn.Softmax(dim=-1)
        self.attn_dropout = nn.Dropout(p=attn_dropout)

    def forward(self, query, key, value):
        dot_product = torch.matmul(query, key.transpose(-2, -1))  # Batch x SeqLength x Channel
        attention_weights = dot_product / self.scale  # Batch x SeqLength x Channel
        attention_weights = self.softmax(attention_weights)  # Batch x SeqLength x Channel
        output = torch.matmul(attention_weights, value)  # Batch x Channel x SeqLength
        output = output * self.scale
        return self.attn_dropout(output), attention_weights


# Initializing the model
m = ScaledDotProductAttention()


