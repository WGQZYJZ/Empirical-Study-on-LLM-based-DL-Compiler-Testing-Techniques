
class AttnLayer(torch.nn.Module):
    def __init__(self, dmodel: int, attn_head: int = 16) -> None:
        super().__init__()
 
        self.dmodel  = dmodel
        self.attn_head  = attn_head
 
        self.kqv_query  = torch.nn.Linear(self.dmodel // self.attn_head, self.dmodel) 
        self.kqv_key    = torch.nn.Linear(self.dmodel // self.attn_head, self.dmodel)
        self.kqv_value  = torch.nn.Linear(self.dmodel // self.attn_head, self.dmodel)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        v1  = self.kqv_query(query).reshape((key.size(0), -1)) @ self.kqv_key(key).reshape((-1, 4)).transpose(-2, -1)
        v2  = torch.softmax(v1 / math.sqrt(self.dmodel // self.attn_head), dim=-1) 
        v3  = torch.dropout(v2 + value, p=0.5) 
        return v3


# Initializing the model
attnlayer1  = AttnLayer(48*8*2, attn_head=16)

