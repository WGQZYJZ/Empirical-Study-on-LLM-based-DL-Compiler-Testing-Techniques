
class Model(torch.nn.Module):
    def __init__(self, dim=256, nhead=8):
        super().__init__()
        self.q = torch.nn.Linear(dim, dim)  # Linear layer for the query tensor with dimensionality of `dim`
        self.k = torch.nn.Linear(dim, dim)  # Linear layer for the key tensor with dimensionality of `dim`
        self.v = torch.nn.Linear(dim, dim)  # Linear layer for the value tensor with dimensionality of `dim`
 
    def forward(self, query_tensor):
        scaled_qk = torch.matmul(query_tensor, k.transpose(-2, -1)) * scale_factor 
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk @ v  # Compute the dot product of the dropout output and the value tensor 
        return output


# Initializing the model
m  = Model()


# Inputs to the model
q1  = torch.randn(64, 256)
__output__  = m(q1)

