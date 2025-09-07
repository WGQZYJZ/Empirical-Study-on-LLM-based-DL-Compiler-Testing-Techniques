

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self,  key, query, scale_factor=1., dropout_p = .5): 
        v2  = torch.matmul(query, key) # Compute the dot product of the query and key tensors
        v3  = v2 * scale_factor # Scale the dot product by a factor 
        v4  = v3.softmax(-1) # Apply softmax to the scaled dot product
        v5  = torch.nn.functional.dropout(v4, p=dropout_p) # Apply dropout to the softmax output
        v6  = v2.mul(value) # Compute the dot product of the dropout output and the value tensor
        return v6

# Initializing the model
m1 = Model()


# Inputs to the model 1
__key__ = torch.randn(30, 512, 84, 97)
query_tensor_1  = torch.randn(30, 8, 64, 84, 97)
value_tensor = torch.randn(30, 84, 84, 97)

 # Model 1 output  
output__model1__  = m1(__key__, query_tensor_1 )


# Inputs to the model 2 (different from the previous one)
key_tensor_2  = torch.randn(30, 514, 87, 96)
query_tensor_2  = torch.randn(30, 84, 64, 87, 96)

 # Model 2 output  (different from the previous one as well)
output__model2__  = m1(key_tensor_2 , query_tensor_2 )

