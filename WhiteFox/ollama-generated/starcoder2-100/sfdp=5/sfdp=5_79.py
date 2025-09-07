
class Model(torch.nn.Module):
    def __init__(self, embedding_size = 32, hidden_size=64):
        super().__init__()
        self.embedding_layer  = torch.nn.Linear(785 * 785 , embedding_size)
        self.gru = torch.nn.GRUCell(hidden_size + embedding_size, hidden_size)
 
    def forward(self, x):
        v1  = self.embedding_layer(x).view(-1, 785 * 785 , -1) # Embedding layer
        v2  = torch.dropout(v1, p=0.3, inplace=False)# Dropout layer (with customizable dropout ratio p=0.3)
        v3  = self.gru(v2, hidden_state) # GRU layer
        return v3
 
model = Model()

