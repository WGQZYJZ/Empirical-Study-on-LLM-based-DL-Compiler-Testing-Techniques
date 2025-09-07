
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(512, 384)
 
    def forward(self, x1, x2):
        qk = self.matmul(x1).transpose(-2, -1) * (x2 ** 0.75)
        scaled_qk = qk / (qk.sum(-1) + 1e-6) # Scale the dot product by a factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.4) # Apply dropout to the softmax output
        output = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and the value tensor
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(512, 64, 384)
x2 = torch.randn(64, 64, 512)
