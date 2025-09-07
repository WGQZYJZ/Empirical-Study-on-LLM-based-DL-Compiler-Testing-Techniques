
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):

        v1  = torch.matmul(input1, input2.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v2  = v1.div(scale_factor)                           # Scale the dot product by a given scale factor
        v3  = torch.nn.functional.softmax(v2)                 # Apply softmax to the scaled dot product
        v4  = dropout(v3, p=dropout_p)                        # Apply dropout with probability of 0.1 and the dropout tensor as input 
        v5  = v4.matmul(input2)                              # Compute the dot product between the value and dropout tensors

        return v5

# Initializing model