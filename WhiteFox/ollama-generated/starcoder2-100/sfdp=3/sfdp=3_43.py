
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.randn(128, 768) / math.sqrt(768)
        self.key  = torch.randn(128, 768) / math.sqrt(768)
        self.scale_factor  =  0.95
        self.dropout_p  =  0.3
 
    def forward(self, value):
        qk  = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk  = qk * scale_factor
        softmax_qk  = scaled_qk.softmax(dim=-1) 
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return dropout_qk.matmul(value)


# Initializing the model
m  = Model()

 # Inputs to the model
 query  = torch.randn(128, 768) / math.sqrt(768) 
 key  = torch.randn(128, 768) / math.sqrt(768) 
 value  = torch.randn(128, 50 * 50, 4096)

__output__  = m(value)

