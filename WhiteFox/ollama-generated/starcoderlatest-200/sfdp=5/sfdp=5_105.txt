
class Model(torch.nn.Module):
    def __init__(self, dim_qkv=None, dropout_p=0):
        super().__init__()
        dim_qkv = 16 if dim_qkv is None else dim_qkv
        self.query = torch.nn.Linear(dim_qkv, dim_qkv) # query projection layer
        self.key = torch.nn.Linear(dim_qkv, dim_qkv)     # key projection layer
        self.value = torch.nn.Linear(dim_qkv, dim_qkv)   # value projection layer
        self.dropout_p = dropout_p
 
    def forward(self, q, k, v):
        x1  = torch.einsum('bdij,bjdl->bdil', q, self.query).transpose(-2,-1)  # Compute the dot product of the query and projection weights
        x2  = torch.einsum('bdij,bild->bdij', k, self.key)                         # Compute the dot product of the key and projection weights
        attn_weights = torch.einsum('bdil,bdij->bdbl', x1, x2) / math.sqrt(q.size(-1))  # Compute the scaled dot product and scale it
        attn_weights = attn_weights + torch.ones_like(attn_weights).to(torch.float32).detach() * -1e9   # Add a small negative number to masked elements in the input tensor
        attn_weights = F.softmax(attn_weights, dim=-1)  # Compute softmax of scaled dot product and scale it
        attn_weights = torch.dropout(attn_weights, self.dropout_p, True)   # Apply dropout to softmax output
        x3  = torch.einsum('bdbl,bild->bdij', attn_weights, v).transpose(-2,-1)    # Compute the dot product of the attention weights and projection weights
        return x3


# Inputs to the model
q = torch.randn(4, 8, 64, 64)
k = torch.randn(3, 8, 64, 64)
v = torch.randn(2, 8, 64, 64)


# Initializing the model
m = Model(dim_qkv=100, dropout_p=0.1)
