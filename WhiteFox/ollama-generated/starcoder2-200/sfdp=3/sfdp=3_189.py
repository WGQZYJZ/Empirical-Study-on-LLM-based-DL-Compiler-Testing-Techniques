
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(32, 4)
        self.key   = torch.nn.Linear(32, 10)
        self.value = torch.nn.Linear(512, 8)
        self.scale_factor  = float(torch.__version__[0]) if int(float(__version__.split(".")[1])) >= 9 else 6
        self.dropout_p = 0.7
 
    def forward(self, query):
        qk  = torch.matmul(query, key.transpose(-2, -1)) / self.scale_factor
        softmax_qk = qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output      = dropout_qk.matmul(value) 
        return v5
 

# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(1024, 32)
