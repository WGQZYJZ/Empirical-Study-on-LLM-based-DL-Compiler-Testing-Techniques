
class Attention(torch.nn.Module):
    def __init__(self, num_heads: int = 8) -> None:
        super().__init__()
 
        self.num_heads  = num_heads
        self.scale      = torch.rsqrt(torch.tensor(1024**-0.5))
 
    def forward(self, query: TensorType, key: TensorType, value: TensorType): 
        batchsize  = query.shape[0]
        # Calculate scaled dot product attention
        inv_scale        = self.scale * math.sqrt(query.size(-1))
        dot              = torch.bmm(query, key.transpose(-2, -1) / inv_scale)
        attention_weights = dot.softmax(dim=-1)
        output           = attention_weights.matmul(value)
 
        return output


# Initializing the model
m  = Attention()
 
# Inputs to the model
key      = torch.randn((50, 8, 64))
query    = torch.randn((32, 8, 16))
value    = torch.randn((32, 8, 32))
 
output   = m(query=query, key=key, value=value)

