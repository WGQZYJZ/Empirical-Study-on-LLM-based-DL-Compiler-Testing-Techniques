
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1): 
        qk = torch.matmul(q1, k1.transpose(-2, -1)) 
        scaled_qk  = qk.div_(scale) # Scale the dot product by a pre-defined factor
        softmax_qk  = scaled_qk.softmax(-1) # Apply softmax to the dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.3) 
        output  = dropout_qk @ v1 
        return output

# Initializing model
m  = Model() 

# Inputs for the model
q1  = torch.randn(256, 49, 875) # Batch size of 256, 49 heads with a sequence length of 875
k1  = torch.randn(256, 49, 875) # Batch size of 256, 49 heads with a sequence length of 875
v1  = torch.randn(256, 875, 300)# Batch size of 256 and the sequence length is 875 with embedding dimensions 300

 # Calculating the output from the model
__output__  = m(q1, k1, v1)