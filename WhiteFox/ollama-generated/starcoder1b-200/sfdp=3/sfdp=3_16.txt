
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Embedding(10, 64) # Embedding layer
        self.key   = torch.nn.Embedding(20, 16)
        self.value = torch.nn.Embedding(20, 32)
        self.scale_factor = torch.tensor(0.5).view(-1, 1, 1)
 
    def forward(self, x1):
        # Query embedding layer
        query  = self.query(x1[:,:,:,None].transpose(-2,-1))
        # Key embedding layer
        key    = self.key(x1[:,:,:,:].transpose(-2,-1))
        # Value embedding layer
        value  = self.value(x1[:,:,None,None])
        # Scale the dot product by a factor
        scaled_qk = query.mul(self.scale_factor)
        # Apply softmax to the scaled dot product
        softmax_qk = scaled_qk.softmax(dim=-1)
        # Apply dropout to the softmax output
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        # Compute the dot product of the dropout output and the value tensor
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(3, 10, 64, 64)
