
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, dropout_p=0.5, inv_scale_factor=4):
        v3  = torch.matmul(x1, x2) / (inv_scale_factor) 
        v6  = v3.softmax(-1)
        v7  = torch.nn.functional.dropout(v6, p=0.5)  
        return v7


# Initializing the model