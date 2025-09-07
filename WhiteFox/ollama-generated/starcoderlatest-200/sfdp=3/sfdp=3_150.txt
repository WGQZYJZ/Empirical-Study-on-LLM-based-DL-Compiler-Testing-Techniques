
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.rand(3, 2, dtype=torch.float))
        self.key = torch.nn.Parameter(torch.rand(3, 3, dtype=torch.float))
 
    def forward(self, x1):
        qk = torch.matmul(x1, self.query)
        softmax_qk = torch.softmax(qk, dim=-1) # Softmax function
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.3)
        output = torch.matmul(dropout_qk, self.key)
        return output

# Initializing the model
m = Model()

