
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, query, key, attn_mask):
        v1 = self.conv(query)
        v1 = F.normalize(v1, p=1, dim=-1)
        v2 = self.conv(key)
        v2 = F.normalize(v2, p=1, dim=-1)
        qk = torch.matmul(v1, v2.transpose(-2,-1)) / math.sqrt(v1.size(-1)) # Compute the dot product of the query and key, and scale it
        qk += attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ v2
        return output


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(16, 3, 160, 160)
key  = torch.randn(16, 8, 80, 80)
attn_mask = (attn_mask == 0).float() # Set the attention mask to all ones where attn_mask==0 and zeros otherwise
