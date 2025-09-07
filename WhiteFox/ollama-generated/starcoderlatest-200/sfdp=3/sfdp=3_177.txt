
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_attention = torch.nn.Linear(1024, 1024)
 
    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2,-1)) 
        scaled_qk  = qk.mul(scale_factor) 
        softmax_qk  = scaled_qk.softmax(dim=-1) 
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        output = dropout_qk.matmul(value)
        return output

 # Initializing the model
m = Model()
 
 # Inputs to the model
x1 = torch.randn(16, 512, 7, 7)
x2 = torch.randn(16, 512, 3, 3)
