
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(2048, 65536)
 
    def forward(self, q, k, v):
        query_vector = self.attn(q).unsqueeze(-1) # Get the embedding of each word in question
        context_vectors = self.attn(k) # Get the embeddings of the words from database
        softmax_qk = torch.nn.functional.softmax(query_vector @ k.transpose(-2, -1), dim=-1) # Compute dot product and get attention weights for query-key pairs in question
        attention_output = softmax_qk @ v # Attend on the different parts of the words from database with corresponding attentions
        return (attention_output * v).sum(dim=2) # Multiply all elements in attention output by value and sum across last dimension


# Initializing the model
m = Model()

# Inputs to the model
q  = torch.randn(1, 32, 65536)  # query word embeddings (batch_size, length, embedding_dimension)
k  = torch.randn(1, 48, 65536)  # key word embeddings (batch_size, length, embedding_dimension)
v  = torch.randn(1, 2048, 65536) # value word embeddings (batch_size, num_heads, sequence_length, embedding_dimension / num_heads)
