
import torch, math
 
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, embed_dim: int = 768, num_heads: int = 12):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        assert self.head_dim * num_heads == embed_dim, 'embed_dim must be divisible by num_heads'
 
        self.scale  = 1 / math.sqrt(self.head_dim)
        self._reset_parameters()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        batch_size, len0, _ = query.shape
        _, _, len1 = key.shape
 
        if key.shape != (batch_size, len1, self.embed_dim):
            raise RuntimeError(f"Expected 3d tensor for key but got: {key.shape}")
 
        attn = torch.einsum('nqhd,nkhd->nhqk', query / self.scale, key)
        attn += self.attn_mask
        attn = F.softmax(attn.clamp(-1e9), dim=-1)  # clamp
        attn = F.dropout(attn, p=0.15, training=self._is_training())
 
        output = torch.einsum('nhqk,nvhkd->nqhd', attn, value)
        return output
 
    def _reset_parameters(self):
        bound = 0.1 / math.sqrt(self.embed_dim)
        self.scale.data.uniform_(-bound, bound)

# Initializing the model
m  = MultiHeadAttention()

 # Inputs to the model
query = torch.randn(256, 78490)
key = torch.randn(256, 78490)
 
