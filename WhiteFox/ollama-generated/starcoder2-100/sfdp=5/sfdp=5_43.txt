
class AttentionModel(torch.nn.Module):
    def __init__(self, dropout=0.1):
        super().__init__()
 
        self._query = torch.nn.Linear(64, 32) 
        self._key = torch.nn.Linear(512, 32)
        self._value = torch.nn.Linear(512, 384)
        self._dropout = torch.nn.Dropout(dropout_p=dropout)
 
    def forward(self, query):
        key = self._key(query).transpose(-2,-1)
 
        # compute the dot product of the query and the key (plus an attention mask)
        qk  = torch.matmul(query, key)/ math.sqrt(query.size(-1))
 
        qk  += torch.ones_like(qk)
 
        # apply dropout to the result of the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1) 
        attn_weight  = self._dropout(attn_weight)
 
        # compute the output as the dot product between the attention weights and the value.
        output   = torch.matmul(attn_weight, self._value(query))
        return output

# Initialize the model
model  = AttentionModel()

# Input to the model
input1  = torch.randn(32, 64) # Generate an input tensor with a shape of (batch size=32 x 64) for the first parameter of the forward pass method


