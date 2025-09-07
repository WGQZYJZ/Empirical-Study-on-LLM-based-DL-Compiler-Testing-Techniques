
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        query  = x1
        key     = x1 + 1
        attn_mask = torch.zeros_like(query) # Set the attention mask for the input

        attn_weight  = torch.softmax(query @ key.transpose(-2, -1) / math.sqrt(key.size(-1)), dim=-1) # Compute softmax and then compute scaled dot product
        output       = attn_weight @ x1 # Compute weighted sum of value (in this case the identity function)

        return output

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
