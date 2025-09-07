
class Model(torch.nn.Module):
    def __init__(self, query_size: int, key_size: int, value_size: int, hidden_dim: int):
        super().__init__()
        self.matmul = torch.nn.Linear(query_size + key_size, hidden_dim) # Linear layer with input dimension of 2*hidden_dim
        self.softmax = torch.nn.Softmax()
        self.dropout = torch.nn.Dropout(dropout_p)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model with public PyTorch APIs
m1 = Model(query_size=256, key_size=256, value_size=256, hidden_dim=1024)

