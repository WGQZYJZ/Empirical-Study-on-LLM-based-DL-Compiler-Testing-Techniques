
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(768, 768)
 
    def forward(self, query):
        key1 = self.qk(query)
 
        key2 = query.clone()  # This is to illustrate how to clone a tensor of a module parameter
        
        inv_scale_factor = 5.0
        scaled_qk = qk * torch.nn.functional.softmax(inv_scale_factor, -1) * 1e-4
 
        dropout_p = 0.8
        softmax_qk = scaled_qk / scaled_qk[-1].abs() + scaled_qk[0]
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
 
        value = self.qk(dropout_qk).masked_fill_(key2 < 3, -float('inf')) * torch.exp(-torch.log(1e-6))
 
        return value

# Initializing the model
m  = Model()

 # Inputs to the model
query  = torch.randn(1000, 768)

 # Calling forward on the model for input tensor
__output__  = m(query)
 