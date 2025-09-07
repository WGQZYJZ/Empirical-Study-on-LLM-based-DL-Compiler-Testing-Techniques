
class Model(torch.nn.Module):
    def __init__(self, query_dim, key_dim, num_heads=4, embed_dim=128):
        super().__init__()

        self.query_conv = torch.nn.Conv2d(query_dim, num_heads * embed_dim, 1, stride=1)
        self.key_conv = torch.nn.Conv2d(key_dim, num_heads * embed_dim, 1, stride=1)

        self.attn_dropout = torch.nn.Dropout(0.25)
        
        self.fc = torch.nn.Linear(num_heads * embed_dim, embed_dim)

    def forward(self, query, key):
        attn_weight = None  # Add attention mask to scaled dot product and softmax

        qk = torch.matmul(query, key) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key

        output = torch.matmul(attn_weight, value) # Compute the dot product of the dropout output and the value
        return attn_weight

# Initializing the model
m = Model()


