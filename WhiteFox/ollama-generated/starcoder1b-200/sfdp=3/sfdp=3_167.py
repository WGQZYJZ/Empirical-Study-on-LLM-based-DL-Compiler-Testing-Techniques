
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(64, 256)
        self.key   = torch.nn.Linear(64, 256)
        self.value = torch.nn.Linear(256, 2)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scale_factor = self.training # Calculate a scale factor for the dot product before applying softmax, and dropout to this value
        qk = qk / scale_factor               # Scale the dot product by a factor
        softmax_qk = F.softmax(qk, dim=-1)   # Apply softmax to the scaled dot product
        dropout_qk = F.dropout(softmax_qk, p=0.5)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(x2)       # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


