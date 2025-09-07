
class Model(torch.nn.Module):
    def __init__(self, hidden_dim1=32, hidden_dim2=64):
        super().__init__()
        self.hidden_layer  = torch.nn.Linear(3 * (8**2), hidden_dim1) 
        self.output_layer = torch.nn.Linear(hidden_dim1, hidden_dim2)
        self.dropout = torch.nn.Dropout(0.5)
 
    def forward(self, x):
        h  = self.hidden_layer(x).relu()
        y  = h.view(-1, 3 * (8**2)) # Flattening the hidden layer output
        h1 = self.dropout(h)
        h2 = self.output_layer(h1).relu() 
        return h2


# Initializing the model