
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 0.1
        self.dropout = 0.5
 
    def forward(self, query, key, value):
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) * scale
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout)
        output  = dropout_qk.matmul(value) 
        return output


# Initializing the model
m  = Model()
 
 # Inputs to the model
x1  = torch.randn(8, 64, 320, 7695 ) 
 x2  = torch.randn(8, 64, 320,  1) 
 x3  = torch.randn(8, 64, 320, 30500 )
 
 # Running the model on inputs
output  = m(x1, x2, x3)