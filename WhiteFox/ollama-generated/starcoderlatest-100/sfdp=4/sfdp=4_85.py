
class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, attn_mask):
        # YOUR CODE HERE: 
        
        return output
    
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.query = torch.nn.Linear(1000, 512)
        self.key   = torch.nn.Linear(1000, 512)
        self.value = torch.nn.Linear(1000, 512)
        self.attn_mask = torch.ones_like(self.query)

        # YOUR CODE HERE: 
        self.attention = SelfAttention()

    def forward(self, x):
        v1 = self.query(x)
        v2 = self.key(x)
        v3 = self.value(x)
        return self.attention(v1, v2, self.attn_mask)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2048, 1000)
