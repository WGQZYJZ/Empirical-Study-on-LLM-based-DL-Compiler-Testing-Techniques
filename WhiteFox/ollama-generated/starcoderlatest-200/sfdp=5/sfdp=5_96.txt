
class Model(torch.nn.Module):
    def __init__(self, n_head):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(32, n_head)
        self.pool = torch.nn.AdaptiveAvgPool2d((1, 1))
 
    def forward(self, q, k, v):
        attn_output, _ = self.attn(q, k, v) # Compute the attention weights and apply the attention mask to them
        output = self.pool(attn_output).squeeze(-1).squeeze(-1) # Average over the last two dimensions to get a vector
        return output

# Initializing the model
m = Model(n=4)


# Inputs to the model
q = torch.randn(2, 32, 64, 64)
k = torch.randn(2, 32, 64, 64)
v = torch.randn(2, 32, 64, 64)


