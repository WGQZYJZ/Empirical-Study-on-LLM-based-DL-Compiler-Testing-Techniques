
class Model(torch.nn.Module):
    def __init__(self, inv_scale_factor=1., scale_factor=None):
        super().__init__()
        self.query  = torch.nn.Parameter(torch.randn(32)) # query tensor of size (32)
        self.key   = torch.nn.Parameter(torch.randn(64, 32)) # key tensor of size (64, 32)
        self.value = torch.nn.Parameter(torch.randn(32, 16)) # value tensor of size (32, 16)
 
    def forward(self):
        qk  = query * key  # Compute the dot product of the query and key tensors
        scaled_qk = qk / scale_factor if scale_factor is not None else qk.div(inv_scale_factor) # Scale the dot product by an inverse or a fixed scale factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product 
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.)  # Dropout is applied and does not drop any elements
        output   = dropout_qk.matmul(value)  # Compute the dot product of the dropout output with value tensor
        return output
# Initializing the model
m1  = Model()
m2  = Model()

