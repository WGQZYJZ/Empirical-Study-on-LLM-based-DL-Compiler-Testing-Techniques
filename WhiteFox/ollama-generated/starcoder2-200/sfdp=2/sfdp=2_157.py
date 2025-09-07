
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8) 
        self.key = torch.nn.Linear(4, 12)
        self.value = torch.nn.Linear(5, 6)
        self.dropout_p = 0.9

    def forward(self, x):
        query = self.query(x)
        key = self.key(torch.ones([x.size()])) # A random tensor
        value = self.value(torch.ones([x.size()]).mul(5))
        qk = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk  = qk / math.sqrt(4)
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  
        output = dropout_qk.matmul(value)
        return output

# Initializing the model
m  = Model()

# Inputs to the model
x = torch.randn(1000, 4, 32, 80) 

__output__  = m(x)

