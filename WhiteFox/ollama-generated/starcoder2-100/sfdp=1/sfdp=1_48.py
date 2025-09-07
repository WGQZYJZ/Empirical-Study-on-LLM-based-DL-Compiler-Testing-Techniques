
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn((8, 3054))) 
        self.key   = torch.nn.Parameter(torch.randn((8, 216947))
        self.value = torch.nn.Parameter(torch.randn((16, 216947)))
 
    def forward(self):  
        qk  = torch.matmul(query, key.transpose(-2,-1))
        scaled_qk = qk / inv_scale_factor 
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        output  = dropout_qk.matmul(value)
        return output


# Initializing the model