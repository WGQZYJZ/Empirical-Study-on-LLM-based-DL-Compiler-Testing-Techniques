
class AttentionModel(torch.nn.Module):
    def __init__(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask: torch.BoolTensor, dropout=0.5) -> None:
        super().__init__()
        self._query  = query
        self._key  = key
        self._value  = value
        self._attn_mask  = attn_mask
        self._dropout  = torch.nn.Dropout(p=dropout, inplace=False)
 
    def forward(self):
        v1  = (self._query @ self._key.transpose(-2, -1)) / math.sqrt(torch.size(self._query)[-1]) # Apply the dot product of the query and key to compute the softmax
        v1  += torch.BoolTensor(self._attn_mask) # Add the attention mask to the scaled dot product
        v2  = F.softmax(v1, dim=-1) # Apply the softmax operation on the result 
        v3  = self._dropout(v2) # Apply dropout to the softmax output
        v4  = torch.bmm(v3,self._value)# Compute the dot product of these attention weights and the value
        return v4
 
# Initializing the model
m1  = AttentionModel(torch.randn(20,64), torch.randn(20,64,50), torch.randn(20,50))

