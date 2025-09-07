
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(8, 3))
        self.key = torch.nn.Parameter(torch.randn(8, 3))
 
    def forward(self, x1):
        query_tensor = self.query # Get the query tensor from the model's parameters
        key_tensor = self.key # Get the key tensor from the model's parameters
        qk  = torch.matmul(query_tensor, key_tensor)
        scaled_qk = qk / math.sqrt(32)
        softmax_qk = scaled_qk.softmax()
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1) # Apply dropout to the output of softmax
        output = query_tensor * 3 + key_tensor * 7 + dropout_qk
        return output

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
m = Model()
output = m(x1) # The final output of the model is a tensor with 256 elements


