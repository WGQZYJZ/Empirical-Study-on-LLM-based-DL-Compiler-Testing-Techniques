
class Model(torch.nn.Module):
    def __init__(self, num_heads=8, d_k=64):
        super().__init__()
        self.head = torch.nn.Linear(d_v, num_heads * d_k)
 
    def forward(self, x1):
        q = x1  # Query
        k = x1  # Key
        v = x1  # Value
        n = x1.size(0)  # Number of sentences
        k = torch.reshape(k, (n, -1, self.num_heads, self.d_k))  # Expand the dimension to a new rank with the number of heads in it
        scaled_qk = torch.matmul(q, k).div(torch.linalg.det(torch.eye(self.num_heads) * (self.scale_factor)))  # Compute the dot product
        dropout_qk = torch.nn.functional.dropout(scaled_qk.softmax(-1), p=dropout_p)  # Apply dropout to the softmax output
        out = dropout_qk.matmul(v).contiguous().view(n, self.num_heads, -1)  # Compute the dot product of the dropout output and the value
        return out


# Initializing the model
m = Model()


