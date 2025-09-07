
class Model(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()
        self.d_model = d_model
        self.embedding = torch.nn.Embedding(vocab_size, embedding_dim)  # Embedding layer for the vocabulary
        self.pos_enc = PosEncLayer(d_model, dropout_p=0.)  # Positional encoding layer
        self.fc = nn.Linear(d_model, 128)  # Final fully connected layer
 
    def forward(self, x):
        if isinstance(x, str):
            x = torch.tensor(vocab[x], dtype=torch.long).unsqueeze(0).unsqueeze(1)  # Embed the word in the vocabulary
            x += self.embedding(x)  # Add to the embedded data
        else:
            x = self.embedding(x)  # Add to the embedded data
 
        h = F.gelu(self.fc(self.pos_enc(x)))  # Forward pass through a fully connected layer
        return h


# Initializing the model
m = Model()

# Inputs to the model
sentence1 = 'Hi!'
sentence2 = 'What do you think?'
