
class Model(torch.nn.Module):
    def __init__(self, dim, nhead):
        super().__init__()
        self.dim = dim
        self.query  = torch.nn.Linear(dim, nhead * dim)
        self.key    = torch.nn.Linear(dim, nhead * dim)
        self.value  = torch.nn.Linear(dim, nhead * dim)
        self.softmax = nn.Softmax(dim=-1)
 
    def forward(self, x):
        query = self.query(x)
        key   = self.key(x)
        value = self.value(x)
        scaled_query  = query.div(torch.exp(-0.5 * torch.einsum('bh,bhi->bhl', key, query)))
        softmax_query = self.softmax(scaled_query)
        dropout_qk    = nn.functional.dropout(softmax_query, p=dropout_p)
        output        = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model(dim=8, nhead=4)


