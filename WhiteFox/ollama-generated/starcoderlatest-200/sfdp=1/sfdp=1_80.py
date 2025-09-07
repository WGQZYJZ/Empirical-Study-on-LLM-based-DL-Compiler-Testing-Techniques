
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax = torch.nn.Softmax(-1)
 
    def forward(self, q1, k1, v1):
        v1  # Not used in this pattern
        softmax_qk = self.softmax((q1.matmul(k1).transpose(-2, -1)) / scale_factor)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = (dropout_qk @ v1).transpose(-2, -1)  # Compute the dot product of the dropout output and the value tensor
        return output

# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(1024, 64, 1, 1)
k1 = torch.randn(1024, 64, 1, 1)
v1 = torch.randn(1024, 32, 8, 8)
