
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, scale=None):
        v1  = torch.matmul(x1, x2.transpose(-2, -1)) 
        if scale is not None:
            v1  /= scale
        v2  = v1.softmax(dim=-1)
 
        if scale is not None:
            v3  = torch.nn.functional.dropout(v2, p=0.5, training=self.training)
            v4  = v3.matmul(x1)
        else:
            v3  = v2.matmul(x1)
            v4  = v3.div(scale)
 
        return v4

# Initializing the model
m  = Model()
 
# Input tensors to the model
i_tensor1  = torch.randn(64, 1024) # Generate a random tensor of shape (64 x 1024)
i_tensor2  = torch.randn(1024, 2038) # Generate a random tensor of shape (1024 x 2038)
 
# Scale factor to use with the dot product of the query and key tensors. This is the same as above: scale_factor = 5
scale_factor  = torch.tensor(5, dtype=torch.float64).cuda() 
 
# Setting the dropout probability. Since it is set in the call to the module's forward method, it won't be modified during training. 0.1 in this case is just for demonstration purposes.
dropout_p = 0.2
 
# Calculating outputs from the model using the input tensors and the scale factor
