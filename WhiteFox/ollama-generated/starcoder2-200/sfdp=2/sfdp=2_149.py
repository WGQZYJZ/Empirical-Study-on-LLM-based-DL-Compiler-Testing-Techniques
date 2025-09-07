
class Model(torch.nn.Module):
    def __init__(self, inv_scale_factor, dropout_p=0., **kwargs):
        super().__init__()
        self.inv_scale_factor  = torch.tensor([float(inv_scale_factor)])
        self.query  = torch.nn.Parameter(torch.randn(48))
        self.key  = torch.nn.Parameter(torch.randn(61, 32))
        self.value  = torch.nn.Parameter(torch.randn(50, 73, 93))
 
        self.softmax_qk  = torch.nn.Softmax(-1)
        self.dropout  = torch.nn.Dropout(p=float(dropout_p))
 
    def forward(self):
        vq  = torch.matmul(self.query, self.key.transpose(-2, -1)) # Compute the dot product of the query and the key
        svq  = vq / self.inv_scale_factor[0] # Scale the dot product by the inverse scale factor
        svqk  = softmax(svq) # Apply softmax to the scaled dot product
        dvqk  = self.dropout(svqk).matmul(self.value) # Apply dropout to the softmax output, and then compute the dot product of the dropout output and the value
 
        return dvqk


# Initializing the model
m  = Model(0.2538964176987983, dropout_p=0.)

