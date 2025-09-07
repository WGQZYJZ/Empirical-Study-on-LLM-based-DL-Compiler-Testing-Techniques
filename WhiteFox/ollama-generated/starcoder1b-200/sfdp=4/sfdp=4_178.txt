
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        query = torch.randn(10, 4, 64, 64)
        key   = torch.randn(10, 4, 64, 64)
        value = torch.randn(10, 4, 64, 64)
        attn_mask = (x2 > 0).float().unsqueeze(dim=-2) # Add a 1 to the entries of attention mask. The 1 will be used as the mask.
        attn_weight = torch.softmax(attn_mask * query, dim=-1)  # Apply softmax to the scaled dot product
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()
x1 = torch.randn(10, 4, 64, 64)
x2 = torch.randn(10, 4, 64, 64)
