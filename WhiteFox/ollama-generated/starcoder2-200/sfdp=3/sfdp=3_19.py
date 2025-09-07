
class Model(torch.nn.Module):
    def __init__(self, scale=2048., dropout=0.5):
        super().__init__()
        self.scale  = torch.tensor(scale)
        self.dropout  = dropout
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor): 
        v1  = torch.matmul(query, key.transpose(-2, -1)) 
        v2  = v1 * self.scale 
        v3  = v2.softmax(dim=-1)
        v4  = nnf.dropout_impl_(v3, p=self.dropout_, training=self._is_training) # Note that dropout is implemented in the nnF core library
        v5  = v4.matmul(value) 
        return v5

# Initializing the model
m  = Model()


# Inputs to the model