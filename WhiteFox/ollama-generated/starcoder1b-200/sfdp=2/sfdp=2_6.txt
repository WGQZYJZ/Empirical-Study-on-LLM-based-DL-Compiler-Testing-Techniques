
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk  = torch.nn.Linear(768, 10)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 768, requires_grad=True)
output1 = m(x1)
print(output1)


