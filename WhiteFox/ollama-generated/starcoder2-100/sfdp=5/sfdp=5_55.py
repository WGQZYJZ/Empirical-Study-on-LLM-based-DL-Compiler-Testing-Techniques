
class TransformerEncoderLayer(torch.nn.Module):
    def __init__(self, hidden_dim, n_head=4, attn_dropout=0., feedforward_dropout=0., dropout1=0., dropout2=0.):
        super().__init__()
 
        self.attn = torch.nn.MultiheadAttention(hidden_dim, n_head)

        self.fc1  = nn.Linear(hidden_dim, hidden_dim * 4)
        self.dropout1  = nn.Dropout(dropout1)
        self.relu = nn.ReLU()
        
        self.fc2  = nn.Linear(hidden_dim*4, hidden_dim)
        self.dropout2  = nn.Dropout(dropout2)

    def forward(self, x):
        # Compute dot product of query and key, plus dropout, mask, and scaling
        attn_mask = (x[:, None] < 0).type_as(x) * (-1e9 - 1)
        qk = self.attn(query=x, key=x)[0].to(dtype=x.dtype)

        # Compute softmax of dot product to get attention weights and dropout
        attn_weight = torch.softmax(qk + attn_mask, dim=-1)
        attn_weight  =  torch.dropout(attn_weight, p=0.35)
        
        # Get the output from attn weight, add residual connection, feed forward, dropout, relu and a norm layer
        # x_new = self.attn(query=x, key=x)[0] * dropout(softmax(qk, dim=-1))
        output  = torch.add(attn_weight @ x)

        # Add residual, dropout, and relu to feed forward
        # feedforward = self.fc2(self.dropout(self.relu(self.fc1(output))))
        output = self.relu(self.fc2(self.dropout2(output)))
        return output


# Initializing the model
n_head  =  4
hidden_dim  =  50
ff_dim = hidden_dim*8
encoderlayer  = TransformerEncoderLayer(hidden_dim, n_head)
 
