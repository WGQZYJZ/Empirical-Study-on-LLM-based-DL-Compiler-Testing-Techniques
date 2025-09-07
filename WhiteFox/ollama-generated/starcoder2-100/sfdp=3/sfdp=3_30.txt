
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 10

    def forward(self, query_, key_, value_):
        vq = torch.matmul(query_, key_.transpose(-2,-1)) # Compute the dot product of the query and key tensors
        vqScaled = vq * self.scale # Scale the dot product by a factor
        vqSoftmax = vqScaled.softmax(dim=-1) # Apply softmax to the scaled dot product
        vqDropout = torch.nn.functional.dropout(vqSoftmax, p=0.5) # Apply dropout to the softmax output
        vqOutput = vqDropout.matmul(value_) # Compute the dot product of the dropout output and the value tensor
        return vqOutput
