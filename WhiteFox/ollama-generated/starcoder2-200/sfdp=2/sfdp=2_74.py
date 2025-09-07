
class Model(torch.nn.Module):
    def __init__(self, scale):
        super().__init__()
        self.scale = scale
        self.inv_scale  = torch.div(1., self.scale)
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v2  = v1 * self.inv_scale
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=0.5)
        __output__  = v4.matmul(value)
        return __output__


m  = Model(768.) # This is the scale factor which will be used to scale the dot product during model inference. You are not allowed to change this value when generating a new PyTorch model for you.