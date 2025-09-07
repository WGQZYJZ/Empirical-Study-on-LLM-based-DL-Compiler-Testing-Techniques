
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.w_query = torch.nn.Linear(1, 8)
        self.w_key   = torch.nn.Linear(1, 8)
        self.w_value = torch.nn.Linear(1, 32)
 
    def forward(self, x):
        v1 = self.w_query(x).view(-1, 8) # Get the query and scale it
        v2 = self.w_key(x).view(-1, 32).transpose(0, 1) # Get the key and transpose it
        v3 = self.w_value(x).view(-1, 32) # Get the value tensor
        attn_weight = torch.softmax((v1 @ v2.t()) / math.sqrt(v1.size(-1)), dim=-1) # Compute the dot product of query and key and scale it
        output = attn_weight @ v3  # Compute the weighted sum of value
        return output
# Initializing the model
attn = Attention()

# Inputs to the model
x = torch.randn(6, 8, 1)
