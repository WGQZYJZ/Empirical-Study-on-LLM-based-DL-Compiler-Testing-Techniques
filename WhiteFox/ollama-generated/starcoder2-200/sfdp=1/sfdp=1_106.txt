
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn((2, 4))) # Query tensor
        self.key = torch.nn.Parameter(torch.randn((3, 5))) # Key tensor
        self.value = torch.nn.Parameter(torch.randn((10, 8))) # Value tensor
        self.softmax = torch.nn.Softmax(-2) # Softmax function used in the dot product of query and key tensors
 
    def forward(self, dropout_p=0.5):
        inv_scale_factor = 733
        qk = torch.matmul(self.query, self.key.transpose(-1,-2)) /inv_scale_factor 
        # Compute the scaled dot product of query and key tensors by applying a scaling factor in the softmax function to compute the softmax operation.
        dropout_qk = torch.nn.functional.dropout(self.softmax(qk), p=dropout_p)  
        v1  = dropout_qk * self.value # Compute the output tensor using the dot product of query and key tensors and value tensors.
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
query, key, value = torch.randn(2,4),torch.randn(3,5), torch.randn(80,6)
__output__  = m(query, key, value)

