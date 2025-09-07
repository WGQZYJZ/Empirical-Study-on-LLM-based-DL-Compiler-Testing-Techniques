
class Model(torch.nn.Module):
    def __init__(self, d_k=64, d_v=64, dropout_p=0.1):
        super().__init__()
 
        self.fc = torch.nn.Linear(d_model, d_k)  # Linear projection from the embedding space to the query and key
        self.norm1 = nn.LayerNorm(d_k)
        self.dropout = nn.Dropout(p=dropout_p)

        self.fc2 = torch.nn.Linear(d_k, d_v)  # Linear projection from the query and key to the output space
        self.norm2 = nn.LayerNorm(d_v)
 
    def forward(self, x1, x2):
        x1 = self.dropout(self.norm1(self.fc(x1)))  # The hidden state after applying GRU to the input
        x2 = self.dropout(self.norm2(self.fc2(x2)))  # The output of the GRU is a linear projection from the last layer
        return torch.cat([x1, x2], dim=-1)


# Initializing the model
m = Model()


