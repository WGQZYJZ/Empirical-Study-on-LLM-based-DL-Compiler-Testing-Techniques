
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk  = torch.matmul(x1, x1.transpose(-2, -1))
        scaled_qk  = qk / (1e-6 + torch.rsqrt(torch.diagonal(qk))) # Scale the dot product by the inverse scale factor
        softmax_qk = F.softmax(scaled_qk, dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = F.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output

# Initializing the model
m = Model()


