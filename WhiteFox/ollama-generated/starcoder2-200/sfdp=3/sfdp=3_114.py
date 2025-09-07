
class Model(torch.nn.Module):
    def __init__(self, scale_factor: int = 1, dropout_p=0.2):
        super().__init__()

        self.scale_factor  = torch.tensor([scale_factor])
        
        self.dropout = torch.nn.Dropout(dropout_p)

        self.weight  = torch.zeros((48*3, 64))
        
        self.bias    = torch.randn(48).sub_(0.15258789)
        
    def forward(self, query):
        k = self.weight
        v = torch.ones_like(k)

        qk  = torch.matmul(query, k.transpose(-2, -1))
        scaled_qk  = qk.mul_(self.scale_factor) 
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk  = self.dropout(softmax_qk)

        output = dropout_qk @ v

        return output

# Initializing the model
model  = Model()

# Inputs to the model
query = torch.rand(2, 48*3).cuda()
__output__  = model(query)