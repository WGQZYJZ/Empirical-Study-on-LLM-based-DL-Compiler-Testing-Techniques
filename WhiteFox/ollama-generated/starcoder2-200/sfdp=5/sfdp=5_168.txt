
class Model(torch.nn.Module):
    def __init__(self, embedder):
        super().__init__()
        self.query  = torch.nn.Linear(240, 512) # linear layer
        self.key = torch.nn.Linear(240, 512) 
        self.value = torch.nn.Linear(368, 768)
        self.attn_mask = torch.nn.Parameter(torch.zeros([1, 91, 91]))
 
    def forward(self, attn): # (batch size x n tokens x 240)
        query  = self.query(attn).transpose(-2, -1)  # Apply linear transformation to the input. Transpose the result.
        key   = self.key(attn).transpose(-2, -1) 
        value  = torch.relu_(self.value(attn))  # Relu function is used on the output of the linear transformation
 
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk  = qk + self.attn_mask
        
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight  = torch.dropout(attn_weight, dropout_p=0.25, training=self._training)

        output   = attn_weight @ value

        return output
