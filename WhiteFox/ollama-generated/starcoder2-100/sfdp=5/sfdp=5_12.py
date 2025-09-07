
class Model(torch.nn.Module):
    def __init__(self, embedding_dim = int, num_heads = int, hidden_dim = int):
        super().__init__()
        self.embedding  = torch.nn.Embedding(vocab_size + 1 , embedding_dim) # Create an embedding layer with a given dimensionality (the total number of words in the dictionary plus one for unknown words). 
        self.transformer  = torch.nn.Transformer(d_model=embedding_dim, nhead=num_heads, num_encoder_layers=6, dim_feedforward=hidden_dim) # Create a transformer model with 1 encoder layer
        self.linear  = torch.nn.Linear(int(embedding_dim), vocab_size + 1 ) # Create a linear layer that maps the output of the transformer to logits

    def forward(self, src):
        embedding  = self.embedding(src) 
        tgt  = torch.zeros([embedding.shape[0], embedding.shape[-2]], dtype=torch.int64) 
        out_transformer  = self.transformer(embedding, tgt)
        logits = self.linear(out_transformer[:, -1]) # Pick the output of the transformer at the last position. Note that -1 refers to the final position of the embedding matrix (the penultimate position is -2).
        return logits


# Initializing the model 
m = Model() 

# Inputs for the model 
src  = torch.tensor([[5, 6]], dtype=torch.int64)
__output__  = m(src)
 
