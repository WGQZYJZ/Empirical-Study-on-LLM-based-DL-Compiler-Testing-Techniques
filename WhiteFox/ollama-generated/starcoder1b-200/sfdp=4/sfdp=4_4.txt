
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, key_tensor):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1
        v6 = v2 * v5
        attn_weight = torch.softmax(qk, dim=-1) @ value # Compute the dot product of the attention weights and the value
        return (attn_weight * value).sum(-1) # Sum over all dimensions except for the batch dimension


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
key_tensor = torch.randn(1, 8)
