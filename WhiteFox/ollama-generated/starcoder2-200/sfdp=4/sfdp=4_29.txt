
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(64, 128)

    def forward(self, query, key, value, attn_mask=None):
        output, attn_weights  = self.attn(query, key, value, attn_mask)
        return output


# Initializing the model
m  = Model()

# Inputs to the model
key  = torch.randn(16, 32, 80, 59) # Input tensor of key with shape [batch size, embedding size, length, width]
value  = torch.randn(16, 32, 80, 59) # Input tensor of value with shape [batch size, embedding size, length, width]
query  = torch.randn(16, 4, 17) # Input tensor of query with shape [batch size, head count, length]
attn_mask  = torch.zeros(235890, 17) # Attention mask


# Final output of the model
out  = m(query, key, value, attn_mask=attn_mask)

