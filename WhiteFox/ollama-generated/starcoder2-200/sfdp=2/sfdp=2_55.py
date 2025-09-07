
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.1):
        super().__init__()
        self.softmax = torch.nn.Softmax(dim=-1)
 
        # Parameters
        scale  = .5 ** (.75 * 64)  # Inferred as .5 ** (0.75 * 2) = 0.3981071705534973 / 64 = .00437550
        inv_scale  = 1./ scale  # Computed as 1/.00437550 = 23777.7255
        
        self.key  = torch.randn(8, 64) 
        self.value  = torch.randn(8, 64)
        self.query  = torch.randn(8, 16*64) # Change size of query and the value to match query_tensor
 
        # Dropout
        self.dropout = torch.nn.Dropout(p=dropout_p)
 
    def forward(self): 
        qk  = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk  = qk.div(inv_scale)
        softmax_qk  = self.softmax(scaled_qk) # Change softmax to self.softmax
        dropout_qk  = self.dropout(softmax_qk) 
        output  = dropout_qk @ value  # Change the dot product to dropout_qk.matmul(value)
        return output
