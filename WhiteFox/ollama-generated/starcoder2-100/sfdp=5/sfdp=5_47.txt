
class TransformerModel(torch.nn.Module):
    def __init__(self, num_encoder_layers=6, input_dim=512, hidden_dim=512):
        super().__init__()

        self._input = torch.nn.Linear(in_features=input_dim, out_features=hidden_dim)
        self._transformer  = torch.nn.TransformerEncoderLayer(d_model=hidden_dim, nhead=8)
        self._output = torch.nn.Linear(in_features=hidden_dim, out_features=2048)
 
        self.dropout = torch.nn.Dropout(p=0.1)
 
    def forward(self, query):
        attn_mask  = torch.triu(torch.ones((query.size(-3), query.size(-3)), device=query.device)).masked_fill_(torch.tril(torch.ones_like(attn_mask)) == 1)

        v0  = self._input(query)
        v0  = self.dropout(v0)
        v1  = torch.nn.TransformerEncoderLayer(d_model=self._input, nhead=8)(v0)
        return v1

# Initializing the model
m  = TransformerModel()

