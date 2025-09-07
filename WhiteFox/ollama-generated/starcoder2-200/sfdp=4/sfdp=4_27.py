
class Attention(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
 
        self.query = torch.nn.Parameter(config["model"]["key"], requires_grad=True)
        self.key  = torch.nn.Parameter(config["model"]["key"], requires_grad=False)
        self.value = torch.nn.Parameter(config["model"]["value"], requires_grad=True)
        self.attn_mask = torch.nn.Parameter(config["model"]["attnMask"], requires_grad=False)
 
    def forward(self, query):
        v1  = query @ self.key.transpose(-2,-1) / math.sqrt(query.size(-1))
        v3  = v1 + self.attn_mask 
        v5  = torch.softmax(v3, dim=-1)
        v7  = v5 @ self.value
        return v7


m  = Attention({
  "model": {
    "key": torch.randn([64,9,8]),
    "value": torch.randn([2048,9,1]),
    "attnMask": torch.randn([64,5,3]) 
  }
})

x  = m(torch.randn([17, 1]))
