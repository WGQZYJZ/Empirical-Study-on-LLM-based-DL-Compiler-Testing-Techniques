
class Attention(torch.nn.Module):
    def __init__(self, num_heads: int = 8):
        super().__init__()
        self.num_heads = num_heads
 
    def forward(query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask: torch.Tensor) -> torch.Tensor:
        query = query / math.sqrt(query.size(-1)) # Compute the scaled dot product of the query and key
        query = query + attn_mask  # Add the attention mask to the scaled dot product
        qk = query @ key.transpose(-2, -1)
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output
class Model(torch.nn.Module):
    def __init__(self, num_heads: int = 8):
        super().__init__()
        self.attention = Attention(num_heads)
 
    def forward(query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask: torch.Tensor) -> torch.Tensor:
        output = self.attention(query, key, value, attn_mask)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
