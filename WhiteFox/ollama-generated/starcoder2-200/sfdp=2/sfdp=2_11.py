
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.scale  = torch.nn.Parameter(data=1e-6 * torch.ones((8,)), requires_grad=True)
 
    def forward(self, query_, key_, value_, dropout_=0.25):
        v1  = torch.matmul(query_, key_.transpose(-2, -1))
        v2  = v1 / self.scale
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=dropout_)
        v5  = v4.matmul(value_)
 
        return v5
 
# Initializing the model
m  = Model()


# Inputs to the model