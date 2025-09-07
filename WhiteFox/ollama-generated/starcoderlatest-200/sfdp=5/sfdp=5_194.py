
class Model2(torch.nn.Module):
    def __init__(self, vocab_size, embed_dim, num_heads):
        super().__init__()
        self.num_layers = 4
        self.layer_norm_0 = torch.nn.LayerNorm((3, 64, 64))
        self.layer_norm_1 = torch.nn.LayerNorm(embed_dim)
        
        # Multi-head attention (qkv)
        self.attn_layer_0 = MultiHeadAttention(embed_dim=embed_dim, num_heads=num_heads)
        
        # Attention pooling layer
        self.attn_pooling = torch.nn.Linear(num_heads * embed_dim, 1)
        
        # Layer normalization
        self.layer_norm_2 = torch.nn.LayerNorm((3, 64, 64))
        
        # FFN and dense connections
        self.ffn = torch.nn.Sequential(
            torch.nn.Linear(embed_dim * 2, embed_dim),
            torch.nn.ReLU(),
            torch.nn.Dropout(0.1),
            torch.nn.Linear(embed_dim, vocab_size)
        )
    
    def forward(self, x1):
        # Multi-head attention (qkv)
        output = self.attn_layer_0(x1).transpose(-2, -3)
        
        # Attention pooling layer
        attn_weights = torch.nn.functional.softmax(
            self.attn_pooling(torch.cat((output[0], output[4]), dim=-1)), dim=-1
        ).unsqueeze(-1)

        # Layer normalization and linear ffn
        output = (self.layer_norm_0(x1 + attn_weights @ output[2])
            * torch.dropout(attn_weights, 0.1, True))
        
        # FFN and dense connections
        output = self.ffn(torch.cat((output[0], output[4]), dim=-1))
        return output


# Initializing the model
m = Model2(vocab_size=35826, embed_dim=768, num_heads=12)
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
