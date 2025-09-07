
class Model(torch.nn.Module):
    def __init__(self, qk_dim=4096, attn_mask=None):
        super().__init__()
        self.query = torch.nn.Linear(qk_dim, qk_dim)
        self.key = torch.nn.Linear(qk_dim, 1 + qk_dim)
        self.attn_mask = attn_mask
 
    def forward(self, v1):
        v2 = self.query(v1)  # Apply the query to the input tensor
        v3 = v2 @ (self.key(v2)).transpose(-2,-1)/ math.sqrt(v2.size(-1)) + self.attn_mask if isinstance(self.attn_mask, torch.Tensor) else 0 
        v4 = torch.softmax(v3, dim=-1).detach()
        v5 = torch.dropout(v4, p=0.1, inplace=True).reshape([*v2.shape[:-1]])
        v6 = self.key(v2) @ v5 + self.attn_mask if isinstance(self.attn_mask, torch.Tensor) else 0 # Compute the dot product of the dropout output and the value
        return v6

# Initializing the model
m  = Model()
 
# Inputs to the model
v1 = torch.randn(48, 2592, 72, 32)

 # Input tensor for m(x1)
__input_tensor__ = torch.randn(48, 2560, 72, 32).to("cuda")

