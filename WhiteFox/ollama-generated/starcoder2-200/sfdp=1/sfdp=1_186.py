
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(torch.rand(1))
        self.dropout = torch.nn.Dropout(0.5)
 
    def forward(self, query, key, value):
        vq = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of a query and a key tensor
        vs  = vq.div(self.scale) # Divide the output by a scale factor
        softmax_vq = vs.softmax(dim=-1) 
        dropout_vq = self.dropout(softmax_vq)
        return dropout_vq.matmul(value)

# Initializing the model