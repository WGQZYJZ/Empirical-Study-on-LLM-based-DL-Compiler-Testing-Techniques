
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(torch.rand(1))
        self.dropout  = torch.nn.Dropout(p=0.5)
 
    def forward(self, xq, xk, v):
        q  = torch.matmul(xq, xk.transpose(-2,-1)) # Compute the dot product of two tensors
        scale_factor  = torch.sigmoid(torch.nn.functional.hardtanh(self.scale, min=0., max=20.))
        scaled_qk  = q * scale_factor 
        softmax_qk  = scaled_qk.softmax(-1) # Apply the softmax to the scaled dot product
        dropout_qk = self.dropout(softmax_qk) # Apply dropout on the softmax output of the scaled dot product
        v2  = dropout_qk @ v
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
 
xq1, xk1, v1 = torch.randn(50), torch.randn(3,4,5), torch.randn(7)
__output__  = m(xq1, xk1, v1)

