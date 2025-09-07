
class Attention(torch.nn.Module):
    def __init__(self, hidden_dim=768, nhead=12):
        super().__init__()
 
        self.qkv  = torch.nn.Linear(hidden_dim, hidden_dim * 3)

        self.attn  = torch.nn.MultiheadAttention(hidden_dim, nhead, dropout=0.1)

        self.fc  = torch.nn.Linear(nhead*hidden_dim, hidden_dim)
 
    def forward(self, x):
        v2  = self.qkv(x)  # Transform the input into three separate tensors (query, key and value). Each tensor is a matrix of shape [B, N, H]
        v3, _, _  = self.attn(v2[0], v2[1], v2[2])

        return self.fc(v3)


# Initializing the model
m  = Attention()

 # Inputs to the model
x  = torch.randn(64, 768)
__output__  = m(x)

