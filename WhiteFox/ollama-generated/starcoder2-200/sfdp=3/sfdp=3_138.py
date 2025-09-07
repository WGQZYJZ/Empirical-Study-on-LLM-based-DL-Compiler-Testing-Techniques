
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        q  = torch.randn(32) # Input to the dot product operator (query tensor)
        k  = torch.randn(8096) # Input to the dot product operator (key tensor)
        v  = torch.randn(4715) # Input to the dot product operator (value tensor)
        # Scaled dot-product attention
        scale_factor = 32 * 4715 ** -0.5
        # Apply dot product operator 
        scaled_qk  = torch.matmul(q, k.transpose(-2, -1)) / ((k**0.5).sum()**-1) 
        # Apply softmax
        softmax_qk  = scaled_qk.softmax(dim=-1)  
        # Apply dropout
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=32 * 4715 ** -0.5)
        output = dropout_qk @ v

        return output


# Initializing the model
m = Model()
 

# Inputs to the model
x1 = torch.randn(128, 16) # Input to the dot product operator (query tensor)
x2 = torch.randn(320974) # Input to the dot product operator (key tensor)
__output__  = m(x1, x2)

