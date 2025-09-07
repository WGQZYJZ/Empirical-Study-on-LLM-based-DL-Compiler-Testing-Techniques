
class AttentionModel(torch.nn.Module):
    def __init__(self, d_key: int = 32, d_query: int = 32, dropout_p: float = 0.5):
        super().__init__()
        self.attention = torch.nn.Sequential(
            torch.nn.Linear(d_key + d_query, d_key * 2), 
            torch.nn.ReLU(),
            torch.nn.Dropout(dropout_p)
        )
 
    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output
 
 # Initializing the model
m = AttentionModel()

 # Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
