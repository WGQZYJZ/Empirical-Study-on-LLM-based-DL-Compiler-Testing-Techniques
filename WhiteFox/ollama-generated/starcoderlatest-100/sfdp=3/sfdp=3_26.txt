
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(1024, 512)
        self.key = torch.nn.Linear(1024, 512)
 
    def forward(self, x1, x2):
        qk = torch.matmul(self.query(x1), self.key.transpose(-2, -1)) * scale_factor
        softmax_qk = qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(self.value, dropout_qk)
        return output
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(16, 1024)
x2  = torch.randn(32, 1024)
