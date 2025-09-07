
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Embedding(n_token, dim)  # Create embedding layer to represent the query tensor
        self.key   = torch.nn.Embedding(n_token, dim)  # Create embedding layer to represent the key tensor
        self.value = torch.nn.Embedding(n_token, dim)  # Create embedding layer to represent the value tensor
 
    def forward(self, x1):
        q1 = self.query(x1)  # Apply the query tensor to the input tensor
        k1 = self.key(x1)   # Apply the key tensor to the input tensor
        v1 = self.value(x1)  # Apply the value tensor to the input tensor
 
        # Compute the dot product of the query and key tensors
        # Scale the dot product by a factor
        # Apply softmax to the scaled dot product
        # Apply dropout to the softmax output
        qk   = torch.matmul(q1, k1.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        qk_scale  = qk.mul(self.scaling)  # Scale the dot product by a factor
        scaled_qk  = qk_scale.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=self.dropout)  # Apply dropout to the softmax output
        output  = dropout_qk.matmul(v1)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
