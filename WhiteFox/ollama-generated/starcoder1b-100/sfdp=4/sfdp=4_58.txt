
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key  = torch.nn.Parameter(torch.randn(3, 4, 5, 6))
 
    def forward(self, x1):
        k = self.conv(x1)  # Compute the dot product of the query and key, and scale it
        qk = k @ self.key.transpose(-2, -1) / math.sqrt(k.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_mask = torch.triu(torch.ones((3, 4)))  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk * attn_mask, dim=-1) # Apply softmax to the result
        output = attn_weight @ x1  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
