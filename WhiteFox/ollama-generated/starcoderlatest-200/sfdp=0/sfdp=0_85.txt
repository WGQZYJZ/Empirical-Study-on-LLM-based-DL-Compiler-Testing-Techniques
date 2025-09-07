
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, heads = 8, dropout = 0.1):
        super().__init__()
        self.heads = heads
 
        # Scaled Dot-Product Attention mechanism
        self.scaled_dot_product = torch.nn.Linear(768, heads * 32)
        self.softmax = torch.nn.Softmax(-1)
 
    def forward(self, q, k, v):
        batch_size, seq_len = q.shape[0], q.shape[1]
 
        # Scaled Dot-Product Attention mechanism (see the model definition above)
        scaled_dot_product = self.scaled_dot_product(torch.cat([q, k, v], dim=-1))
        attention_weights = self.softmax(scaled_dot_product).unsqueeze(dim=1)
 
        # Multiplication and addition operation for calculating attention vector
        context  = torch.matmul(attention_weights, v) 
        output   = torch.sum(context, dim=1)
 
        return output


class Transformer(torch.nn.Module):
    def __init__(self, heads = 8, dropout = 0.1):
        super().__init__()
        self.multihead_attention = MultiHeadAttention(heads=heads, dropout=dropout)
 
    def forward(self, q, k, v):
        return self.multihead_attention(q, k, v)


class Model(torch.nn.Module):
    def __init__(self, heads = 8, dropout = 0.1):
        super().__init__()
        self.transformer = Transformer(heads=heads, dropout=dropout)
 
    def forward(self, x1, x2, x3):
        return self.transformer(x1, x2, x3)


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 768, 1024, 1024)
x2 = torch.randn(1, 768, 512, 512)
x3 = torch.randn(1, 768, 256, 256)
 
