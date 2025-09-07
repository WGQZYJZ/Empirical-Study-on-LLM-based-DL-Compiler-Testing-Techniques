
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
         # Parameters
         inv_scale  = torch.Tensor([0.1])[None]
         dropout_p =  5e-2

         scaled_qk  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
         scaled_qk  = scaled_qk.div(inv_scale)
         softmax_qk = scaled_qk.softmax(dim=-1)
         dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
         output     = dropout_qk.matmul(value)

         return output

 # Initializing the model
m  = Model()

 # Inputs to the model (query, key and value tensors that have been randomized) 
 query1, key1, value1 = torch.randn(4, 320), torch.randn(4, 640), torch.randn(4, 380)
__output_1__   = m(query1, key1, value1)

 # Inputs to the model (query, key and value tensors that have been randomized again; different from above inputs) 
 query2, key2, value2 = torch.randn(4, 380), torch.randn(4, 640), torch.randn(4, 315)
__output_2__   = m(query2, key2, value2)

