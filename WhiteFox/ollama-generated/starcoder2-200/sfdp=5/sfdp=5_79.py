
class Model(torch.nn.Module):
    def __init__(self, qk_dim=1024, nhead=8):
        super().__init__()
 
        self.qkv  = torch.nn.Linear(qk_dim * 3, qk_dim * 3) # The linear layer that combines the query, key and value features
        self.attn  = torch.nn.MultiheadAttention(qk_dim, nhead=8) # Applies multi-head attention to three different subspaces in the query embedding.
 
    def forward(self, x1):
        qkv  = self.qkv(x1).transpose(-2,-3)  # Reshape and transpose the tensor from (..., 3, qk_dim) to (-3 ... ,-2 ...)
        o  = self.attn(qkv)[0].transpose(-3,-2) # Apply the multihead attention operation with the reshaped query key value embedding
        return o


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(4,8,512*3).view(4, -1, 512 * 3)
__output__  = m(x1)

