
class AttentionModel(torch.nn.Module):
    def __init__(self, query: Tensor, key: Tensor, value: Tensor, attn_mask=None) -> None:
        super().__init__()
        self.query = query
        self.key = key
        self.value = value
        self.attn_mask = attn_mask
        self.scale = math.sqrt(query.size(-1))
 
    def forward(self, mask):
        qk = torch.bmm(self.query, self.key.transpose(-2, -1)) / self.scale 
        if self.attn_mask is not None:
            qk += self.attn_mask
        attn_weights  = torch.softmax(qk, dim=-1) 
        attn_output = (attn_weights @ self.value).transpose(-1, -2)
        return attn_output

# Initializing the model
q1  = torch.randn(32,  480,   56,    76 )
k1  = torch.randn(32,  480,     7 ,  76)
v1  = torch.randn(32, 480 * 76,   192)
attn_mask = torch.zeros(32, 56*76, device=q1.device).fill_(torch.tensor(-float("inf")))
m = AttentionModel(query=q1, key=k1 , value=v1 )

