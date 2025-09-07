
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk = self.conv(x1).transpose(-2, -1).contiguous().view(x1.size(0), -1) / math.sqrt(x1.size(2)) # Compute the dot product of the query and key, and scale it
        attn_mask = torch.eye(attn_dim=x1.size(2)).repeat((1, 1, x1.size(1))).type_as(qk) * (1 - mask).unsqueeze(-1) # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        value = self.conv(x1).contiguous().view(x1.size(0), -1) @ attn_weight  # Compute the dot product of the attention weights and the value
        return value

# Initializing the model
m = Model()


