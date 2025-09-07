
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_projection = torch.nn.Linear(8, 1)
 
    def forward(self, query, key, value, scale_factor):
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) / scale_factor # Compute the dot product of the query and the key
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = F.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return attention_projection(dropout_qk.matmul(value))
 

# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(8, 64, 128, 128)
key    = torch.randn(8, 64, 64, 64)
value  = torch.randn(8, 64, 1024, 1024)
scale_factor = torch.randn(1)

