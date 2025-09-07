
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
 
        # Create two linear transformations and one dropout layer
        self.k1 = torch.nn.Linear(in_features=self.embed_dim, out_features=self.embed_dim, bias=False)
        self.q1 = torch.nn.Linear(in_features=self.embed_dim, out_features=self.embed_dim, bias=False)
        self.v1 = torch.nn.Linear(in_features=self.embed_dim, out_features=self.embed_dim, bias=False)
        self.dropout = torch.nn.Dropout(p=0.35)
 
    def forward(self, x): # This method should be implemented
        scaled_dot_product = 1
        