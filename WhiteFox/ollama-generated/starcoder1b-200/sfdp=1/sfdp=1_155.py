
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(32, 64)
        self.key   = torch.nn.Linear(64, 1024)
        self.value = torch.nn.Linear(1024, 256)
        self.scale_factor = torch.nn.Parameter(torch.randn(1), requires_grad=False)
        self.dropout_p = 0.5
 
    def forward(self, x):
        query = self.query(x).contiguous()  # Transpose the input to match with that of the previous layer
        key   = self.key   (x).contiguous()
        value = self.value (x).contiguous()
 
        scale_factor = torch.sigmoid(self.scale_factor)  # Compute the sigmoid at scale_factor
        scaled_query = query.mul_(scale_factor)  # Scale the input query by a factor of the scale_factor
        dropout_qk   = F.dropout(scaled_query, p=self.dropout_p)  # Apply dropout to the input query
 
        softmax_qk  = dropout_qk.mm(key)  # Compute the dot product between the two input tensors using the matrix multiplication and softmax is applied
        dropout_value = F.dropout(softmax_qk.matmul(value), p=self.dropout_p)  # Apply dropout to the softmax output
        output = dropout_value.mul(scale_factor)  # Scale the dot product by a factor of the scale_factor
 
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 32, 64, 64)
y1  = torch.randn(1, 64, 64, 64)
__output__  = m(x1, y1)


