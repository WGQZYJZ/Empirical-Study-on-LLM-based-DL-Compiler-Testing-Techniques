
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(32, 4)
 
    def forward(self, query, key, value):
        v1 = self.attn(query, key, value)[0] # Apply the multiheaded attention to query, key and value tensors
        return v1

# Initializing the model
m = Model()

