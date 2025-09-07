
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.matmul(query, key)
 
    def forward(self, qk):
        scaled_qk  = qk / scale_factor # Scale the dot product by the inverse scale factor 
        softmax_qk  = scaled_qk .softmax(-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk @ value # Compute the dot product of the dropout output and the value tensor 
        return output


# Initializing the model
m = Model()
scale_factor = torch.tensor(0.5)
 
# Inputs to the model
qk  = torch.randn(3, 8)
value = torch.randn(2, 16, 9, 9)
__output__  = m(qk)

