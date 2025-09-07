
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = self.conv(x2)
        qk = torch.cat([v1, v2], dim=-1) / (math.sqrt(v1.size(-1)) * math.sqrt(v2.size(-1)))  # Compute the dot product of the query and key, and scale it
        attn_mask = torch.zeros((x1.size(0), x1.size(1)), dtype=torch.float32, device=m.device)
        attn_mask[range(attn_mask.shape[0]), range(attn_mask.shape[1])] = 1  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        value = torch.sum(attn_weight * x2, dim=-1)  # Compute the dot product of the attention weights and the value
        return value


# Initializing the model
m = Model()
x1 = torch.randn(3, 8, 64, 64)
x2 = torch.randn(3, 8, 64, 64)
