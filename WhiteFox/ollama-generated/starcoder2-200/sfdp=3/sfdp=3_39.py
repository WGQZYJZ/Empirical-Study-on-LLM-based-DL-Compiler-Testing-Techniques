
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax  = torch.nn.Softmax(-1)
 
    def forward(self, query, key, value):
        vq = torch.matmul(query, key.transpose(-2, -1))
        vs  = scale_factor * vq 
        ds  = vq.div(vs) # Avoid using the softmax function for numerical stability in this example
        
        dropout_vq  = torch.nn.functional.dropout(ds, p=dropout_p)
        output  = dropout_vq @ value
        
        return output


# Initializing the model
m = Model()
 
# Inputs to the model (query, key and values tensors of size [batch_size x sequence_length x embedding dimension])
q  = torch.randn(10, 64) # A 3D tensor
k = torch.randn(10, 64, 512).div(32.)
v = k

