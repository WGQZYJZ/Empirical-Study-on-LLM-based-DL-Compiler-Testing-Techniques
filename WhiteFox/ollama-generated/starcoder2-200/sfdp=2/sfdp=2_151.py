
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
       inv_scale  = torch.rand([])
       dropout_p  = torch.rand([])
 
       scaled_qk = torch.matmul(query, key.transpose(-2, -1)).div(inv_scale)
       softmax_qk  = scaled_qk.softmax(dim=-1)
       
       # Dropout implementation 1 
       # dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
       # Dropout implementation 2
       # https://pytorch.org/docs/stable/nn.html#torch.nn.Dropout
       dropout_qk  = torch.nn.functional.dropout(softmax_qk,
                                                 p=dropout_p,
                                                 training=self.training)
 
       output = dropout_qk.matmul(value)
       return output
 
 # Initializing the model
 a = Attention()

 # Inputs to the model
 q1  = torch.rand([32, 48, 64, 64]) 
 k1  = torch.rand([32, 48, 70, 70])
 v1  = torch.rand([32, 96, 64, 64])
  __output__  = a(q1, k1, v1)

