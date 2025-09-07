
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query = torch.nn.Linear(768, 1024)
        self.key = torch.nn.Linear(768, 1024)
        self.value = torch.nn.Linear(768, 1024)
 
    def forward(self, x1):
        v1 = torch.matmul(self.query(x1), self.key.transpose(-2, -1))
        scaled_qk = v1.div(math.sqrt(v1.shape[-1]))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(self.value(x1))
        return output
 
 # Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 24, 768)
