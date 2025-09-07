
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(768, 1024)
        self.attention = torch.nn.MultiheadAttention(embed_dim=1024, num_heads=8)
 
    def forward(self, x1, x2):
        a  = self.linear1(x1) # Project the query and key to hidden size of 1024
        b, c = torch.shape(a)  # Batch size and sequence length of queries
        x  = torch.unsqueeze(torch.arange(b), dim=0).repeat((c, 1)).long()
        y  = self.attention(query=x, key=x1, value=a) # Apply the attention mechanism to compute the context vector
        return y

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(32, 768, 5, 80)
x2 = torch.randn(32, 768, 100, 1)
