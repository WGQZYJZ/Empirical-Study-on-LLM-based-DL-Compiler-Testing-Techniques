
class Model(torch.nn.Module):
    def __init__(self, d_model=1024, nhead=8, num_layers=6, dropout=0.1):
        super().__init__()
        self.d_model = d_model
        self.nhead = nhead
        self.num_layers = num_layers
        self.dropout = dropout
 
        # Initialize the transformer model layers
        self.self  = nn.Linear(d_model, d_model)
        self.query = nn.Linear(d_model, d_model)
        self.key   = nn.Linear(d_model, d_model)
        self.value = nn.Linear(d_model, d_model)
 
        # Initialize the attention mechanism
        self.attn = MultiHeadAttention(d_model=d_model, nhead=nhead)
 
    def forward(self, x1, x2):
        