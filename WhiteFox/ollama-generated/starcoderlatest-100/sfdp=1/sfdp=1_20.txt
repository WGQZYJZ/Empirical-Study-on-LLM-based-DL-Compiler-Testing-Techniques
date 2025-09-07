
class Attention(torch.nn.Module):
    def __init__(self, dim, query_dim):
        super().__init__()
 
        self.linear = torch.nn.Linear(query_dim * 2, dim)
        self.dropout1 = torch.nn.Dropout()
        self.dropout2 = torch.nn.Dropout()
 
    def forward(self, x):
        batch_size, query_len, key_len, embedding_dim = x.shape
        queries = x.view(batch_size, query_len, -1)  # BQ K E
        keys = x.view(batch_size, query_len, -1).permute(0, 2, 1)  # B Q K
        query_keys = torch.cat((queries, keys), dim=-1)  # B Q K (2*E)
        attention_scores = self.linear(query_keys)  # BQ K E
        attention_scores = attention_scores / math.sqrt(embedding_dim)  # Scale dot product by square root of embedding dimension
        attention_scores = F.softmax(attention_scores, dim=-1)  # Apply softmax to the scaled dot product
        output = self.dropout2(torch.matmul(attention_scores, keys))  # Compute the dot product of the dropout scores and the key values
        output = torch.cat((queries, output), dim=-1).view(batch_size, query_len, -1)  # Concatenate queries with outputs
        attention_weights = self.dropout1(F.softmax(attention_scores.view(-1), dim=0))  # Apply softmax to the scaled dot product
        return attention_weights, output


# Attention class instantiated and initialized in the model
self.attention = Attention(dim=embedding_dim, query_dim=query_dim)
 
# Inputs to the model
x1 = torch.randn(1, 4, query_dim)
attention_weights, x2 = self.attention(x1)

 