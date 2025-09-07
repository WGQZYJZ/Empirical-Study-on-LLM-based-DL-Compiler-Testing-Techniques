
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, query, key):
        v1  = torch.matmul(query, key) # Apply matrix multiplication between the query and key tensors
        v2  = scale_factor * v1       # Scale the output of the dot product by a scaling factor
        v3  = v2.softmax(-1)          # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=0.5)    # Dropout the result with probability 0.5
        v5  = dropout_p * v4         # Scale the output of dropout by a factor
        v6  = v5.matmul(value)     # Apply matrix multiplication between the scaled dropout output and value tensor
        return v1,v2,v3,v4,v5,v6

# Initializing model
m = Model()
__query__, __key__, __value__  = torch.randn(8,7), torch.randn(8,9), torch.randn(8,10) # Inputs to the model

# Predicted output of the model
__output_1__,__output_2__,__output_3__,__output_4__,__output_5__,__output_6__ = m(__query__, __key__)

