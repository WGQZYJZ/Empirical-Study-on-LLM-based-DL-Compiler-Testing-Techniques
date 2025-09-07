
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key_conv = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        kq = self.query_conv(x1).matmul(x2.transpose(-2, -1)) # Compute the dot product of x1 and x2
        ks = self.key_conv(x2).transpose(0, 1).contiguous().matmul(x1) # Compute the dot product of x1 and x2 transposed to match (K, S) order of input tensor
        softmax_qk = kq.div(torch.sum(ks * ks, dim=-1).sqrt()) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v = dropout_qk.matmul(x2) # Compute the dot product of the dropout output and x2 tensor
        return v


# Initializing the model
m = Model()

