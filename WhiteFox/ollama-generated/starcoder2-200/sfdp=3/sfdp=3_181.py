
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2):
        v1  = torch.matmul(query1, key2.transpose(-2,-1)) # Compute the dot product of a query tensor and a value/key tensor. 
        v2 = v1.mul(scale_factor) # Scale by a factor in the dot-product of v1 and the resulting tensor
        v3  = v2.softmax(dim=-1) # Apply softmax to the scaled dot product v2, which was produced using the value/key tensors.
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)  #Apply dropout with probability of 0.5 to the tensor v4, which is the result of applying the softmax operation to the scaled dot product
        v6  = v2.matmul(v1)#Compute the dot product of the output of the dropout operation and a query/key tensor
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
query1  = torch.randn(10, 5) # Create a query/key/value tensor for an attention layer with 10 5 dimensional vectors as keys and values. 5 keys, 1 value. Query: 5 dimensional vector. Value: 1 dimensional vector. 1 vector is multiplied by 10. 
key2 = torch.randn(7, 5) # Create another query/key tensor for the attention layer with 3 5 dimensional vectors as keys and values. 3 keys, 7 values. Key: 5 dimensional vector. Value: 5 dimensional vector. 3 values are multiplied by 10.

