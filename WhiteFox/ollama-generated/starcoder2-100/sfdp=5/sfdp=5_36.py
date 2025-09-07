
class TransformerBlock(torch.nn.Module):
    def __init__(self, hidden_size: int, num_heads: int) -> None:
        super().__init__()
 
        self.norm1 = torch.nn.LayerNorm(hidden_size) 
        self.attn = torch.nn.MultiheadAttention(
            embedding_dim=hidden_size, 
            num_heads=num_heads
        )  
        self.norm2 = torch.nn.LayerNorm(hidden_size) 

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask: torch.Tensor):
        
        v1  = self.norm1(query)
        v2  = self.attn(v1, k, q, attn_mask)[0] 
        v3  = self.norm2(v2 + query)
 
        return v3


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.transformer = TransformerBlock(hidden_size=512, num_heads=8)

    def forward(self, qk: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask: torch.Tensor):
        v1  = self.norm1(qk)
        v3  = self.norm2(v2 + query)
 
        return v6

# Initializing the model
m  = Model()
 
# Inputs to the model
q1, k1, v1 = torch.randn(80000, 512), torch.randn(80000, 512), torch.randn(80000, 512)  # Input tensors q, k and value 
attn_mask  = torch.randn((24,37))  # Attention mask

