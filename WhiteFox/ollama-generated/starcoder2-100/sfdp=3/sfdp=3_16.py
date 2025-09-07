

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Input to the model: key and query tensors with shapes [B * num_heads, L] and [B * num_heads, K], respectively; value tensor is of shape [B * num_heads, L, D].
        v2 = self.attn_layer(x1) 
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
qk = torch.randn(30594687*3, 768)/torch.sqrt((3-2)/3).to(device=device), # scale_factor=1/math.sqrt(d_head).to(device=device),
query = torch.randn(30594687*3, 768)/torch.sqrt((3-2)/3).to(device=device)
key = torch.randn(30594687*3, 768)/torch.sqrt((3-2)/3).to(device=device),  # value = query.shape[1] 
scale_factor = torch.tensor([1e-6]).repeat(qk.shape[-1])
dropout_p = torch.tensor([0.9]).to(device=device)

 # Calling the forward method of the model
output__ = m(qk, query, key, value)
