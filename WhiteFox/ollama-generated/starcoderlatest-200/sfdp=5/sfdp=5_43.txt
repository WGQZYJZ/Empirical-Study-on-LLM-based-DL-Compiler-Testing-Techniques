
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.config = config
 
        self.query_layer = torch.nn.Linear(config.embedding_dim, config.hidden_dim)
        self.key_layer = torch.nn.Linear(config.embedding_dim, config.hidden_dim)
        self.value_layer = torch.nn.Linear(config.embedding_dim, config.hidden_dim)
 
        self.attn_weight_layer = torch.nn.Linear(config.hidden_dim, 1)
 
        self.dropout_layer = torch.nn.Dropout(p=config.dropout)
 
    def forward(self, q, k, v):
        qk = (q @ self.query_layer(q)) + (k @ self.key_layer(k))
        attn_weight = self.attn_weight_layer(qk)
        attn_weight = torch.softmax(attn_weight, dim=-1)
 
        output = self.dropout_layer(attn_weight @ v)
 
        return output

 # Input of the model
q  = torch.randn(1, 3, 64, 64)
k  = torch.randn(1, 3, 64, 64)
v  = torch.randn(1, 3, 64, 64)

 # Output of the model
output = m(q, k, v)

 