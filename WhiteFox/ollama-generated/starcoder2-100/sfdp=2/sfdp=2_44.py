
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2):
 
        qk = torch.matmul(query1, key2)
        
        scaled_qk  = 0.5 * qk.div(inv_scale_factor) 
        
        softmax_qk  = scaled_qk.softmax(dim=-1)  
        
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        output = dropout_qk.matmul(value2)

        return output


# Initializing the model
m  = Model()


# Inputs to the model