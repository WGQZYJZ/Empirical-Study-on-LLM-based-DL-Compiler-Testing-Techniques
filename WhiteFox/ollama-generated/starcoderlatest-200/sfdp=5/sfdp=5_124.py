
class Model(torch.nn.Module):
    def __init__(self, hidden_dim=16):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.qkv = torch.nn.Linear(32, 3 * hidden_dim)
 
    def forward(self, x1, x2):
        query = F.gelu(self.qkv(x1)) # Apply gelu activation to the output of linear layer 
        key   = F.gelu(self.qkv(x2)) # Apply gelu activation to the output of linear layer 

        qk  = torch.einsum('b d, c e -> bce', query, key) / math.sqrt(32)
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)

        output  = torch.einsum('b d, c e -> bce', attn_weight, value) 
        return output

 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(32, 3, 64, 64)
x2 = torch.randn(32, 3, 64, 64)
