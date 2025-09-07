
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(32, 1024))
        self.key = torch.nn.Parameter(torch.randn(64, 1024))
        self.value = torch.nn.Parameter(torch.randn(64, 512))
 
    def forward(self):
        qk = torch.matmul(self.query, self.key.transpose(-2, -1))
        scaled_qk = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  
        output = dropout_qk.matmul(self.value) 
        return output

# Initializing the model
m = Model()

