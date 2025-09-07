
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, attn_mask):
        v1 = self.conv(x1)
        v2 = self.conv(x2)
        v3 = torch.mul(v1, attn_mask)
        v4 = torch.mul(v2, attn_weight)
        output = v3 + v4  # Add the two results
        return output


# Initializing the model
m = Model()

