
class Attn(torch.nn.Module):
    def __init__(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> None:
        super().__init__()
        self._query = query
        self._key = key
        self._value = value
 
    @staticmethod
    def scaled_dot(query: torch.Tensor, key: torch.Tensor, scale: float):
         return (query  @  key.transpose(-2, -1)) / math.sqrt(scale)

    def forward(self, attn_mask=None):
        scale = self._key.size(-1)**-0.5
        qk = self.scaled_dot(self._query, self._key, scale)

        if attn_mask is not None:
            qk  += attn_mask
        weight  = torch.softmax(qk, dim=-1) 
        return weight @ self._value


# Initializing the model
attn  = Attn(query, key, value)
 
# Inputs to the model
query  = torch.randn(4, 56, 768)
key  = torch.randn(32, 1096, 768)
value  = torch.randn(4, 128, 768)
 
attn_mask  = torch.zeros([query.size(0), query.size(-2), key.size(-2)])  # Initialize the attention mask to zeros
attn_mask[:, -3:-1]   += 1e9  # Add large numbers (-1e9 to +1e9) to certain positions in the attention mask
 
