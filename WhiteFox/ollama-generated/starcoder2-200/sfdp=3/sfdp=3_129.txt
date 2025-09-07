
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.scale = 1 / math.sqrt(hidden_dim) # Scale factor for dot product
        self.softmax = torch.nn.Softmax(-2, dim=-1)  # Apply softmax to the dot product
        self.dropout = torch.nn.Dropout(p=0.5)
 
    def forward(self, query, key, value):
        scaled_qk  = self.scale * query @ key.transpose(-2, -1) 
        softmax_qk  = self.softmax(scaled_qk) # Apply softmax to the scaled dot product
        dropout_qk  = self.dropout(softmax_qk) # Apply dropout to the softmax output
        v6  = dropout_qk @ value # Compute the dot product of the dropout output and the value tensor
