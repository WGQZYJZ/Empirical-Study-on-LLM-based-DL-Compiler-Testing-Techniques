

class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask: Optional[torch.Tensor] = None) -> None:
        super().__init__()

        self._query  = query 
        self._key   = key
        self._value = value
        self._attn_mask = attn_mask
        self.__output__

    def forward(self):
        qk = torch.matmul(
            self._query, 
            torch.transpose(
                self._key, -2,-1)
        ) / math.sqrt(
            self._query.size(-1))

        if self._attn_mask is not None:
            qk += self._attn_mask

        attn_weight = nn.functional.softmax(qk, dim=-1)
        output  = torch.matmul(attn_weight,self._value)

        return output


# Inputs to the model

key   = torch.randn([4096])
query = torch.randn([4096])
value = torch.randn([4096])
attn_mask  = torch.nn.Parameter(torch.ones((1,32,7,7),dtype=torch.int))

 # __output__  = ScaledDotProductAttention(query, key, value)(attn_mask)
