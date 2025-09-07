
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(torch.tensor([0]))
        self.dropout_p = nn.Dropout(inplace=True)

    def forward(self, query: Tensor, key: Tensor, value: Tensor) -> Tensor:
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk  = qk.mul(scale) # Scale the dot product by a factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = self.dropout(softmax_qk) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output

m  = Model()
m(x1, x2, x3)

