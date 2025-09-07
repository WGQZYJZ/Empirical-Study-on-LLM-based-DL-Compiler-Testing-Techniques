
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0.1)
 
    def forward(self, query, key, value, scale_factor, dropout_p):
        vq  = torch.matmul(query, key.transpose(-2,-1)) # Compute the dot product of two matrices. This pattern characterizes scenarios where the dot product is applied to a query and key tensor.
        sqv = vq * scale_factor 
        softmax_vq  = sqv.softmax(dim=-1) # Apply softmax to the scaled dot product output. This pattern also characterizes scenarios when the softmax function is used on a scaled dot product.
        dropout_vq  = torch.nn.functional.dropout(softmax_vq, p=dropout_p) # Apply dropout to the softmax output. This pattern is similar to the previous one and is common when dropout is used during training of transformer models.
        vv   = dropout_vq.matmul(value) 
        return vv


# Initializing the model
m  = Model()
 
# Inputs to the model
q  = torch.randn(10,256) # Input tensor for a query matrix. This pattern is common when transformer models are used in generative tasks such as language modeling.
k  = torch.randn(10, 256) # Input tensor for a key matrix. This pattern is also similar to the previous one and is common when attention mechanisms used by transformer models are used in generative tasks.
v  = torch.randn(10,256) # Input tensor for a value matrix. This pattern characterizes scenarios where a matrix is multiplied with another matrix.
__scale_factor__ = torch.rand(size=(2)) * (torch.tensor([0])) + torch.tensor([3]) 
__dropout_p__  = 1 - __scale_factor__


__output__   = m(q,k,v,__scale_factor__,__dropout_p__)
