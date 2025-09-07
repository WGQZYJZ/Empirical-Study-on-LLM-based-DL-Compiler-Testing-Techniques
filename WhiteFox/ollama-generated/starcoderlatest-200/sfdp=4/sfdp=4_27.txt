
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, xq, xk, attn_mask):
        vq = self.conv(xq) # Apply pointwise convolution with kernel size 1 to the query tensor
        vk = self.conv(xk).transpose(-2, -1)
        qk = vq @ vk / math.sqrt(vq.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
xq = torch.randn(1, 3, 64, 64)
xk = torch.randn(8, 3, 256, 256)
attn_mask = torch.zeros((8, 1)) # attention mask
