
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value):
        v1  = self.attention(query=query, key=key, value=value)[0] # Compute the output of the multiheaded attention layer
        return v1


# Initializing the model