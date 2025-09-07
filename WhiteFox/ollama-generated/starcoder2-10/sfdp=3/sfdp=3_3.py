
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 3510
        self.dropoutp = 0.7

        self.query = torch.nn.Parameter(torch.randn(2, 4, 6)) # Query tensor
        self.key = torch.nn.Parameter(torch.rand(2, 9, 8)) # Key tensor
        self.value = torch.nn.Parameter(torch.randn(3, 100, 5))

        self.scale_factor = torch.nn.Parameter(self.scale * torch.ones(4,))
        self.dropout_p = torch.nn.Parameter(self.dropoutp * torch.ones(2,))
 
    def forward(self):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax, p=dropout) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor

        return output

m  = Model()

