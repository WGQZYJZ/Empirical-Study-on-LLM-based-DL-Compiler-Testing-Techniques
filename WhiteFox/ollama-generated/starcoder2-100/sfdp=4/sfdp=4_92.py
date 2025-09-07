
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        attn_mask  = torch.zeros_like(x1[:, :, None] + x1[:, None, :])
 
        qk  = x1 @ x1.transpose(-2, -1) / math.sqrt(input.size(-1)) # Compute the dot product of the query and key
        attn_weight  = torch.softmax(qk + attn_mask, dim=-1)  # Apply softmax to the result
 
        return qk, attn_weight
 
 # Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(32, 640, 896)
__output__, attn_weights  = m(x1)