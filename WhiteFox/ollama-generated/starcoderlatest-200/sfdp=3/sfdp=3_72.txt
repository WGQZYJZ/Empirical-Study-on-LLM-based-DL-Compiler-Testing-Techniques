
class Model(torch.nn.Module):
    def __init__(self, embedding_dim, scale=1):
        super().__init__()
        self.scale = scale
 
        # Add two linear layers to map keys and values of queries to query representations and value representations respectively.
        self.query_linear = torch.nn.Linear(embedding_dim, embedding_dim)
        self.key_linear = torch.nn.Linear(embedding_dim, embedding_dim)

        self.attention = MultiHeadAttention(embed_dim=embedding_dim)
 
        # Output layer to map query representations and value representations of different heads to query representation of single head
        self.projection = torch.nn.Linear(2 * embedding_dim, embedding_dim)
 
    def forward(self, x1):
        q1 = F.relu(self.query_linear(x1))
        k1 = F.relu(self.key_linear(x1))
        v1 = self.attention(q1, k1)

        output = torch.cat((q1, k1, v1), dim=-1)
        output = F.relu(self.projection(output))
 
        return output


# Initializing the model
m = Model(embedding_dim=128, scale=0.5)
