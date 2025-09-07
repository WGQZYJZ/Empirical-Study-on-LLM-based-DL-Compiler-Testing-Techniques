
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(32, 64)
        self.key = torch.randn(1024, 32)
        self.value = torch.randn(1024, 64)
        self.dropout_p = torch.nn.Dropout(0.5)
 
    def forward(self):
        qk = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk = qk / math.sqrt(qk.shape[-1])
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        output = dropout_qk @ value
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(32, 64)
        self.key = torch.randn(1024, 32)
        self.value = torch.randn(1024, 64)
        self.dropout_p = torch.nn.Dropout(0.5)
 
    def forward(self):
        qk = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk = qk / math.sqrt(qk.shape[-1])
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        output = dropout_qk @ value

# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(32, 64)
key = torch.randn(1024, 32)
value = torch.randn(1024, 64)
__output__  = m()


