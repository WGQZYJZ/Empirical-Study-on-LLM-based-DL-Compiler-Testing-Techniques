
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul  = torch.nn.functional.matmul
        self.softmax  = torch.nn.functional.softmax

    def forward(self, query, key, value):
        v1 = self.matmul(query, key)
        v2 = v1 * scale_factor 
        v3 = v2.softmax(-1)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p) 
        return self.matmul(v4, value)
        
# Initializing the model with custom hyperparameters: 0.75 for scale factor and 0.1 for dropout probability  
scale_factor  = 0.75
dropout_p  = 0.1
m  = Model()

 # Inputs to the model
query = torch.randn(32, 8*256) * 4 
key = query / scale_factor + 5.5  
value = key / scale_factor / dropout_p
__output__  = m(query, key, value)

