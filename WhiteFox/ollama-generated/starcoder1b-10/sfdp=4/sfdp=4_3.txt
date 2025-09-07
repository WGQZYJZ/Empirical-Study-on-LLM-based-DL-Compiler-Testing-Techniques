
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        query  = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        query = query + attention_mask  # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(query, dim=-1)  # Apply softmax to the result
        value  = torch.matmul(attn_weight, x2)  # Compute the dot product of the attention weights and the value
        return value

# Initializing the model
m = Model()

