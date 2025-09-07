
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.dropout_p = dropout_p
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        scaled_qk = torch.matmul(v1, v1.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        softmax_qk  = scaled_qk.div(torch.norm(scaled_qk, dim=-1).view(1, -1, 1) + 1e-9) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p) # Apply dropout to the softmax output
        v2 = dropout_qk.matmul(x2) # Compute the dot product of the dropout output and the value tensor
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1, x2 = m.forward(torch.randn(1, 3, 64, 64), torch.randn(10, 8))
