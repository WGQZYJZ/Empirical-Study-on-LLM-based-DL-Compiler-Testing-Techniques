
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, key, value, attn_mask):
        v1 = self.conv(x1)
        qk = torch.matmul(v1, key.transpose(-2, -1)) / math.sqrt(key.size(-1))
        # The attention mask is used to prevent attending the positions of zero values in the value tensor
        attn_weight = torch.softmax(qk, dim=-1) * attn_mask  # Apply softmax to the result
        v2 = attn_weight @ value  # Compute the dot product of the attention weights and the value
        output = torch.matmul(attn_weight, v2)  # The weighted sum of the value tensor
        return output


# Initializing the model
m = Model()

