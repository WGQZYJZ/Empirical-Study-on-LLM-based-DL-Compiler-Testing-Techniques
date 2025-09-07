
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Parameter(
            torch.randn([8, 1024], requires_grad=True))
 
    def forward(self, query, value):
        inv_scale_factor = 64
        dropout_p = 0.1
        qk  = torch.matmul(query, self.key) # Compute the dot product of the query and key tensors
        scaled_qk  = qk /inv_scale_factor # Scale the dot product by the inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk @ value # Compute the dot product of the dropout output and the value tensor
        return output

# Initializing the model
m1 = Model()
m2 = Model()
 
# Inputs to the first model
x1, x2 = torch.randn(8, 64), torch.randn(8, 1024)
__output_1__ = m1(x1, x2)
 
# Inputs to the second model
y1, y2 = torch.randn(8, 64), torch.randn(8, 1024)
__output_2__ = m2(y1, y2)

