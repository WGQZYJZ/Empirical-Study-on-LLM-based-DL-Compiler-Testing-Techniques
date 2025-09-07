
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.matmul(x1[0], x1[2].transpose(-2,-1)) # Compute the dot product of the query and key tensors
        scale_factor = 3
        v2  = v1.mul(scale_factor) 
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.3592608748524108)
        output  = dropout_qk.matmul(x[2])
        return output


# Initializing the model
m  = Model()

# Inputs to the model
inp1  = torch.randn(2, 3, 64, 64), torch.randn(7) # The first input tensor has size (2, 3, 64, 64). The second input is a one-dimensional tensor with size 7

 __output__  = m(inp1)
