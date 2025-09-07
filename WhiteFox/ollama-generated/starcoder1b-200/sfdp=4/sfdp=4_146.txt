
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        k = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(torch.prod(x1.size()[-2:]))
        qk = (x1 @ x2.transpose(-2, -1)) / math.sqrt(torch.prod(x1.size()[-2:]))
        attn_mask  = torch.eye(self.num_heads, dtype=torch.float) + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk / math.sqrt(qk.size(-1)), dim=-1)  # Apply softmax to the result
        output  = (attn_weight @ x2).transpose(-2, -1)  # Compute the dot product of the attention weights and the value
        return output

# Initializing the model
m = Model()


