
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, xq, vk):
        v_query  = self.conv(xq)
        qk = v_query @ vk.transpose(-2, -1) / math.sqrt(v_query.size(-1)) + attn_mask # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ vk  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
xq = torch.randn(2, 3, 64, 64)
vk = torch.randn(1024, 8) # (batch_size, embed_dim)
