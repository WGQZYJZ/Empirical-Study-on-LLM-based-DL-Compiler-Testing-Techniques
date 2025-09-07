
class Model(torch.nn.Module):
    def __init__(self, query_layer: torch.nn.Module, key_layer: torch.nn.Module, value_layer: torch.nn.Module):
        super().__init__()
        self.query = query_layer
        self.key = key_layer
        self.value = value_layer
 
    def forward(self, x1, x2):
        qk  = torch.matmul(self.query(x1), self.key(x2).transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return self.value(x2).matmul(dropout_qk) # Compute the dot product of the dropout output and the value


# Initializing the model
query_layer = torch.nn.Linear(...)
key_layer = torch.nn.Linear(...)
value_layer = torch.nn.Linear(...)
m = Model(query_layer, key_layer, value_layer)


# Inputs to the model
x1  = torch.randn(1, query_dim, seq_len, embed_dim)
x2  = torch.randn(1, key_dim, seq_len, embed_dim)
