
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(d_k, d_k)
        self.key   = torch.nn.Linear(d_v, d_k)
        self.value = torch.nn.Parameter(torch.randn(1, 2, d_v, d_k)))
 
    def forward(self, x, key=None):
        if not key:
            return self.forward_features(x)
        else:
            return self.forward_attention(x, key)
    
    def forward_features(self, x):
        # Calculate dot products between query and key tensors (computed here by hand)
        query = self.query(x).transpose(-2, -1)  # Compute the dot product of the input to query and the query tensor
        key    = self.key(key).transpose(-2, -1)     # Compute the dot product of the input to key and the key tensor
        scaled_qk  = torch.matmul(query, key)   # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        value    = dropout_qk.matmul(self.value)   # Compute the dot product of the dropout output and the value tensor
        return value
    
    def forward_attention(self, x, key):
        # Calculate dot products between query and key tensors (computed here by hand)
        query = self.query(x).transpose(-2, -1)  # Compute the dot product of the input to query and the query tensor
        key    = self.key(key).transpose(-2, -1)     # Compute the dot product of the input to key and the key tensor
        scaled_qk  = torch.matmul(query, key)   # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        value    = dropout_qk.matmul(self.value)   # Compute the dot product of the dropout output and the value tensor
        attn     = self.softmax(value)               # Compute attention weights (computed here by hand)
        return torch.matmul(attn, value)        # Compute the weighted sum of the values from the input to the hidden state
