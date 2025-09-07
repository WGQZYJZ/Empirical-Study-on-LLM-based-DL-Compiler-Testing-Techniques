
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(512, 4096)
        self.linear_k = torch.nn.Linear(512, 4096)
        self.linear_v = torch.nn.Linear(512, 4096)
        self.dropout  = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, x):
        q = self.linear_q(x) # Compute the query of shape [batch size, seq len, hidden dim]
        k = self.linear_k(x) # Compute the key of shape [batch size, seq len, hidden dim]
        v = self.linear_v(x) # Compute the value of shape [batch size, seq len, hidden dim]
        query = q.contiguous().view(q.size(0), -1, self.linear_k.in_features)  # Shape: batch size * seq len, hidden dim -> batch size x seq len * hidden dim (with the extra axis of a second)
        key = k.contiguous().view(k.size(0), -1, self.linear_k.in_features) # Shape: batch size * seq len, hidden dim -> batch size x seq len * hidden dim
        scaled_key  = torch.matmul(query, key).div(math.sqrt(self.linear_k.weight.size(-2))) # Compute the dot product of the query and the key, then divide by sqrt(hidden dim)
        softmax_key  = F.softmax(scaled_key, dim=-1)  # Apply softmax to the scaled dot product
        dropout_key  = self.dropout(softmax_key)  # Apply dropout to the softmax output
        value = self.linear_v(dropout_key).contiguous().view(dropout_key.size(0), -1, v.size(-2)) # Compute the dot product of the dropout output and the value, then reshape the result into batch size x seq len * hidden dim
