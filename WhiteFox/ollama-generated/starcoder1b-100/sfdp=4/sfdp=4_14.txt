
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, attn_mask):
        # x1, x2: shape [batch_size, channels, height, width]
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = x2 * (v5 * attn_mask) # Use the dot product of the query and key tensor and multiply by the attention mask
        v7 = v2 * v6
        return v7


# Initializing the model
m  = Model()

