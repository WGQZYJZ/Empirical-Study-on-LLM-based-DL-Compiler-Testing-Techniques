
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key) # Compute the dot product of the query and key tensors
        v2  = v1 / scale_factor # Scale the dot product by the inverse scale factor
        v3  = v2.softmax(-1) # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=0.5) # Apply dropout to the softmax output 
        return v4

# Initializing the model
m  = Model()
 
# Inputs to the model
__input1__  = torch.randn(20, 3, 64, 64), \
              torch.randn(20, 8, 64, 64) ,\
              torch.randn(20, 7, 5, 5) # Generate two query tensors of size (20, 3, 64, 64), and two key tensors of size (20, 8, 64, 64). The model should be different from the previous model.
