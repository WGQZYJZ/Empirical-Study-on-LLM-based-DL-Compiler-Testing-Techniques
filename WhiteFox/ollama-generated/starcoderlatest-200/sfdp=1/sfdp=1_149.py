
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        qk  = torch.matmul(x1, x2.transpose(-2,-1)) # Compute the dot product of the query and key tensors
        scaled_qk  = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(x3) # Compute the dot product of the dropout output and a value tensor
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(8, 64, 64) # N x C x H x W
x2  = torch.randn(100, 64, 64) # M x C x H x W
x3  = torch.randn(100, 512) # D x H' x W'
x4  = torch.randn(100, 100, 128, 64) # T x N x S x C
