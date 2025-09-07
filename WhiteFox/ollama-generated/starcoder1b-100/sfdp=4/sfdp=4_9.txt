
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2, attn_mask=None):
        v1  = self.conv(x1)
        v2  = self.conv(x2)
        v3 = v1 * v2
        # Attention mask is used to control the attention weights of certain positions
        if attn_mask is not None:
            qk  = v3 @ v3.transpose(-2, -1) / math.sqrt(v3.size(-1))
            qk += attn_mask  # Add the attention mask to the scaled dot product
            attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
            output = attn_weight @ v2
        else:
            # Use a simple dot product without attention mask
            v4 = v3 @ v3.transpose(-2, -1) / math.sqrt(v3.size(-1))
            output = v4 @ v2
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
