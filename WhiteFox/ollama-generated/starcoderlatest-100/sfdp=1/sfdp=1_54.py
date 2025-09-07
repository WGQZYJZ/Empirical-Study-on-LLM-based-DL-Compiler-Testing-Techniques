
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0.1)
 
    def forward(self, qk, key, value):
        softmax_qk  = self.dropout(torch.softmax(qk, dim=-1)) # Apply dropout to the output of the dot product of a query and a key tensor
        output  = torch.matmul(softmax_qk, value) # Compute the dot product of the scaled dot product and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
qk = torch.randn(10, 56, 32)
key = torch.randn(10, 48, 16)
value = torch.randn(10, 96, 32)
