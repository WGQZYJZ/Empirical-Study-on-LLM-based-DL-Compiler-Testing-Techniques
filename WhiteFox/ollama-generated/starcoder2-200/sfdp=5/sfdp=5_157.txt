
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(8, 4)
        self.key = torch.nn.Linear(8, 4)
 
    def forward(self, query_tensor):
        v1 = self.query(query_tensor).transpose(-2, -1)  # Compute the dot product of the query and key
        v2 = v1 / math.sqrt(v1.size(-1))  # Scale the dot product
        v3 = torch.nn.functional.pad(v2, [0] * len(query_tensor.size())) + mask
        v4 = torch.softmax(v3, dim=-1)  # Apply softmax to the scaled dot product 
        v5 = torch.dropout(v4, dropout_p, True)  # Apply dropout to the softmax output
        v6 = v5 @ value  # Compute the dot product of the dropout output and the value
