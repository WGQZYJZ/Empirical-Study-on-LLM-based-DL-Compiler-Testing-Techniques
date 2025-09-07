
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        qk = torch.matmul(x1[0], x1[1].transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk / 0.5
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.4)
        output = dropout_qk.matmul(x1[2]) # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m  = Model()

# Inputs to the model
x1  = [torch.randn(3, 64), torch.randn(3, 50, 5)]
x2  = [torch.randn(16) for i in range(2)] # Two separate tensors for query and key values
__output__  = m((x1[0], x1[1]))

