
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
         v1 = torch.matmul(query, key.transpose(-2, -1))
         v2 = v1 / math.sqrt(dim) # Compute the dot product of the query and the key
         v3 = v2.softmax(dim=-1)  # Apply softmax to the scaled dot product
         v4 = torch.nn.functional.dropout(v3, p=0.5)
         return v4.matmul(value)

# Initializing the model
model = Attention()

