
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, k1, v1, attn_mask):
        # Compute the dot product of the query and key
        qk = x1 @ k1.transpose(-2, -1) / math.sqrt(x1.size(-1)) 
        # Add the attention mask to the scaled dot product
        qk += attn_mask 
        # Apply softmax to the result
        attn_weight = torch.softmax(qk, dim=-1) 
        # Compute the dot product of the attention weights and the value
        value = v1 @ attn_weight 
# Initializing the model
m = Model()

