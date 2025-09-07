
class ScaledDotProductAttention(nn.Module):

    def __init__(self):
        super().__init__()
        self._scale = 0.125 ** (3/4)
    
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, mask=None) -> Tuple[torch.Tensor]:
        assert key is not None and value is not None

        attn_score = F.softmax(torch.einsum('bhqd,bhkd->bhqk', [query / self._scale, key]), dim=-1)

        if mask is not None:
            attn_score += mask
        
        attn = torch.einsum("bhqk,bhkd -> bhqd", [attn_score, value])
        return attn


# Initializing the model
m  = ScaledDotProductAttention()

# Inputs to the model
input_tensor = torch.randn(1024, 3897)
query = torch.randn(56, 1024).t() # (batchsize, length, width, height)
key = torch.randn(56, 3897).t() # (batchsize, length, width, height)
value = torch.randn(56, 1024).t() # (batchsize, length, width, height)


