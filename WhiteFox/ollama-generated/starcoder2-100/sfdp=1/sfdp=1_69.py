
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(64, 320)

    def forward(self, x1):
        v1  =  self.qkv(x1)  # Apply the linear layer to the input tensor
        v2  =  qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        v3  =  scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v5  = v2.matmul(v3)  # Compute the dot product of the dropout output and the value tensor
        return v1

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 64)

 __output__  = m(x1)
 
