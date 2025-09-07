
class Model(torch.nn.Module):
    def __init__(self, d_model, nhead=8):
        super().__init__()
        self.d_model = d_model
        self.embedding  = torch.nn.Embedding(10000, d_model)
        self.encoder   = Encoder(nhead, d_model, embedding_dim=self.embedding.weight.size(-1))
        self.fc = nn.Linear(d_model, 1000)
 
    def forward(self, x):
        # Get batch size from the first dimension
        batch_size = x.shape[0]
 
        # Forward pass through encoder
        x = self.embedding(x)
        x = self.encoder(x)
 
        # Retrieve output of last block
        x = torch.stack([self.fc(x).unsqueeze(1) for _ in range(batch_size)], dim=1)
 
# Initializing the model
m  = Model()

