
class Model(torch.nn.Module):
    def __init__(self, dim=None, hidden_size=512, num_layers=6):
        super().__init__()
 
        self.embedding = torch.nn.Embedding(num_embeddings, hidden_size)  # Embedding layer of shape (batch_size, input_length, embedding_dimension)
        self.encoder = EncoderRNN(
            input_dim=dim, hidden_size=hidden_size, num_layers=num_layers
        )
 
    def forward(self, x1):
        x2 = self.embedding(x1)  # Compute the embedding of each sample in batch
        
        # Encode a sequence using gated recurrent units (GRU), 
        # i.e., use a hidden state for every input unit in time step t and a cell state 
        # (a tuple, consisting of two tensors) that is updated as the GRU 
        # learns to make the contextual embedding dependent on the previous
        # output of the model at time step t-1:
        # (hidden_state, hidden_state(t)) = encoder(x(t-1), h(t-1))
        encoder_output, last_hidden  = self.encoder(x2)
 
        return encoder_output, last_hidden


# Initializing the model
m = Model()


