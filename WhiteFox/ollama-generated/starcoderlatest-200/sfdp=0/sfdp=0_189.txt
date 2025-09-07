
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dropout=0.1):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout)
 
    def forward(self, q, k, v, mask):
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(k.shape[-1])
        attention_weights = self.dropout(scores).masked_fill(mask == 0, float('-inf'))
        context = torch.matmul(attention_weights, v)
        return context, attention_weights
 
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, dim, num_heads, dropout=0.1):
        super().__init__()
        self.num_heads = num_heads
        head_dim = dim // num_heads
        self.scale = torch.sqrt(head_dim)
        self.attend = ScaledDotProductAttention(dropout=dropout)
        self.out = torch.nn.Linear(dim, dim)
 
    def forward(self, x1, x2):
        _, num_queries, seq_length, _  = x1.shape
        batch_size = x1.shape[0]
        q = x1.view(batch_size * self.num_heads, seq_length, -1).permute(0, 2, 1)
        k = x2.view(batch_size * self.num_heads, seq_length, -1).permute(0, 2, 1)
        v = x2.view(batch_size * self.num_heads, seq_length, -1).permute(0, 2, 1)
        mask = torch.unsqueeze(x2 != 0, 3)
        attn_output, _ = self.attend(q, k, v, mask)
        x3 = attn_output.view(batch_size, num_queries, seq_length, -1).permute(0, 2, 1, 3).contiguous()
        x4 = self.out(x3)
        return x4
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attn = MultiHeadAttention(dim=512, num_heads=8)
 
    def forward(self, x1, x2):
        output  = self.multihead_attn(x1, x2)
        return output

 # Initializing the model
m = Model()
 
 # Inputs to the model
x1 = torch.randn(10, 32, 768, device="cuda")
x2 = torch.randn(10, 768, 1605, device="cuda")
