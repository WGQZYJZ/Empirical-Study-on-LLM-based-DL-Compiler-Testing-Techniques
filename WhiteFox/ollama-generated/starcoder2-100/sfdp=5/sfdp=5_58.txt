
class SelfAttention(nn.Module):
    def __init__(self, embedder=None):
        super().__init__()
 
        self.query = nn.Linear(2048, 512) # Create a linear layer with the specified input and output dimensions
        self.key = nn.Linear(2048, 512) 
        self.value = nn.Linear(2048, 512) 
        self.attn_mask = torch.nn.Parameter(torch.zeros([36*36])) # Create a parameter that represents the attention mask
 
        nn.init.xavier_uniform_(self.query.weight)
        nn.init.xavier_uniform_(self.key.weight)
        nn.init.xavier_uniform_(self.value.weight)
 
    def forward(self, x1):

        v3 = x1.reshape(-1, 2048).transpose(-1,-2) 
        v6 = torch.nn.functional.linear(v3 ,self.query.weight,None, self.query.bias)
        v7 = nn.ReLU()(v6 + (1 - attn_mask)) * math.sqrt(512 / 512)

        v8 = torch.nn.functional.linear(v4 .transpose(-2,-3),self.key.weight,None, self.key.bias)
        v9 = nn.ReLU()(v7 + (1 - attn_mask)) * math.sqrt(512 / 512)

        v10 = torch.nn.functional.linear(v8 ,self.value.weight,None, self.value.bias)
 
        v12 = v9 @ v10
        return v12
