class Attention(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.scale  = (embed_dim)**-0.5
 
        self.key  = torch.nn.Linear(embed_dim, embed_dim) 
        self.query  = torch.nn.Linear(embed_dim, embed_dim)
        self.value  = torch.nn.Linear(embed_dim, embed_dim)
 
    def forward(self, x1):
        v2  = self.key(x1).transpose(-1, -2) 
        v3  = self.query(x1)
        v4  = self.scale * torch.matmul(v3, v2) # Compute the dot product of the query and key tensors, scaled by a factor
        v5  = torch.nn.functional.softmax(v4, dim=-1) 
        v6  = torch.nn.functional.dropout(v5, p=0.8) 
        v7  = self.value(x1).matmul(v6) # Compute the dot product of the dropout output and the value tensor
        return v7


# Initializing the model
m  = Attention(embed_dim=24)
 
# Inputs to the model
x1  = torch.randn(5, 32, 8, 96)
__output__  = m(x1)

