
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.functional.dropout
        self.softmax = torch.nn.Softmax(-1)
 
    def forward(self, query, key, value, inv_scale_factor=0.5, dropout_p=0.87):
        v1  = self.matmul(query @ key.transpose(-2, -1), p=dropout_p).softmax(dim=-1) 
        v2  = torch.nn.functional.dropout(v1, p=dropout_p)
        __output__  = v2 @ value
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
 query  = torch.randn(3, 4, 5).div_(0.7869114)
 key    = torch.randn(3, 5, 4).div_(1.204401)
 value  = torch.randn(3, 4, 4).div_(1.3771042379)

 # Initializing the model with a forward call to get initial intermediate tensors
__output__   = m(query, key, value)
