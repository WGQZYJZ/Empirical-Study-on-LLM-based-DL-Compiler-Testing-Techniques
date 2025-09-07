
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 512)
        self.key   = torch.nn.Linear(512, 512)
        self.value = torch.nn.Linear(512, 512)
        self.scale = nn.Parameter(torch.zeros(1))
        self.shift = nn.Parameter(torch.zeros(1))
 
    def forward(self, query_key, attn_mask):
        d_k    = torch.sum(query_key * self.key, dim=-1, keepdim=True)  # (batch_size x n_heads x seq_length x hidden_size)
        dk     = d_k  / torch.sqrt((self.key.size(-1))**0.5)
        d_k    = dk * self.scale + self.shift  # (batch_size x n_heads x seq_length x hidden_size)
        q      = self.query(query_key)
        attn   = torch.matmul(q, dk.transpose(-2, -1))
        attn   = attn / torch.sqrt((self.key.size(-1))**0.5)  # (batch_size x n_heads x seq_length x seq_length)
        attn_weight = torch.softmax(attn, dim=-1)  # (batch_size x n_heads x seq_length x seq_length)
        value   = self.value(query_key)  # (batch_size x hidden_size)
        return attn_weight @ value  # (batch_size x hidden_size)


# Initializing the model
m = Model()

