
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        qk = x1 @ x1.transpose(-2, -1) / math.sqrt(x1.size(-1))
        qk += attention_mask.float()
        attn_weight = F.softmax(qk, dim=-1)
        output = (attn_weight * v5).sum(-1) # Sum the weighted sums of all values, resulting in the hidden state of shape (B, C)
        return output


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
