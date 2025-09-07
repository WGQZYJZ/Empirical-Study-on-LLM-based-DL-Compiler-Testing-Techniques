
class Model(torch.nn.Module):
    def __init__(self, vocab_size, embedding_dim=128):
        super().__init__()
        self.query = torch.nn.Embedding(vocab_size, embedding_dim)  # Compute word embeddings from the vocabulary list
        self.key   = torch.nn.Linear(embedding_dim, embedding_dim) # Compute key vectors using a linear layer
        self.value = torch.nn.Linear(embedding_dim, embedding_dim) # Compute value vectors using a linear layer
 
    def forward(self, inputs):
        q = self.query(inputs[:, 0])  # Extract the first word from the input sequence
        k = self.key(q).transpose(-1, -2)   # Compute the key vector for each of the word tokens
        v = self.value(inputs[:, 1]) # Extract the second word from the input sequence
        attn = torch.mm(k, v.transpose(0, 1)) # Calculate attention weights using a pointwise dot product
        output = torch.matmul(attn, v)   # Compute the value vector using the attention weight
        return output

# Initializing the model
m = Model(26)

