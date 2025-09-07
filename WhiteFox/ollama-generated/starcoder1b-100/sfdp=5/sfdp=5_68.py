
class Model(torch.nn.Module):
    def __init__(self, num_layers=2, hidden_dim=64, num_heads=8):
        super().__init__()
        self.num_layers = num_layers
        self.d_k = 1 / math.sqrt(hidden_dim)
        self.scale = 1 / math.pow(hidden_dim, 0.5)
        self.head_dim = hidden_dim // num_heads
 
        self.query = torch.nn.Linear(hidden_dim, hidden_dim, bias=True)
        self.key = torch.nn.Linear(hidden_dim, hidden_dim, bias=True)
        self.value = torch.nn.Linear(hidden_dim, hidden_dim, bias=True)
 
        for i in range(self.num_layers):
            setattr(self, 'layer{}'.format(i + 1), torch.nn.Linear(
                num_heads * head_dim, num_heads * head_dim, bias=False))
 
    def forward(self, x1, x2):
        b = x1.shape[0]
 
        # Compute query and key
        q = self.query(x1).reshape((b, -1, self.num_heads, self.head_dim)).contiguous()  # [b * num_heads, seq_len, head_dim]
        k = self.key(x2).reshape((b, -1, self.num_heads, self.head_dim)).contiguous()  # [b * num_heads, seq_len, head_dim]
        dk = q @ k.transpose(-2, -1) * self.scale  # [b * num_heads, seq_len, head_dim]
 
        # Compute query attention weights
        attn_weight = torch.softmax(dk, dim=-1)  # [b * num_heads, seq_len, seq_len]
        attn_mask = torch.unsqueeze((1 - attn_weight).type(torch.cuda.FloatTensor), 0).to(x1.device)  # [1, b * num_heads, seq_len, seq_len]
 
        # Compute value attention weights
        output = self.value(x2).reshape((b, -1, self.num_heads, self.head_dim)).contiguous() @ attn_weight  # [b * num_heads, seq_len, head_dim]
 
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
x2 = torch.randn(10, 3, 64, 64)
