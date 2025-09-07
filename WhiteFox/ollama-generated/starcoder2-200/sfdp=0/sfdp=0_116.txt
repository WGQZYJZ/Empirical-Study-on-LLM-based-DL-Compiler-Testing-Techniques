

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qry, ky):
        scaled = torch.matmul(qry, ky.transpose(-2, -1)) / inv_scale
        att_weights = scaled.softmax(dim=-1)
        return att_weights


# Initializing the model
m  = Model()

 # Inputs to the model
 qry = torch.randn(3, 4, 56, 56)
 ky = torch.randn(2, 3, 879015)
 
 