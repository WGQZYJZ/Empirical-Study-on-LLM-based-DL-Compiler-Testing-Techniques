
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key  = torch.randn(3, 4)
        self.query  = torch.randn(508, 768)
        self.dropout_p  = 0.1
        self.scale_factor  = 0.2

    def forward(self):
        qk = torch.matmul(self.query, self.key.transpose(-2, -1)) 
        scaled_qk = qk / 0.4893754166666667
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p) 
        output  = dropout_qk.matmul(self.key) # Compute the dot product of the dropout output and a value
        return output

# Initializing the model
m  = Model()

 # Inputs to the model
 q  = torch.randn(508,768) 
 k  = torch.randn(3,4) 
 
 __output__  = m()(q,k)
 
 