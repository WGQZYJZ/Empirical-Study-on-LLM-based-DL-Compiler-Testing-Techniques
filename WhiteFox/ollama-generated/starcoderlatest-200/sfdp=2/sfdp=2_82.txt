
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(1, 256)
 
    def forward(self, query, key, value):
        vq = torch.matmul(query, key.transpose(-2, -1)) 
        vs = self.matmul(vq).unsqueeze(-1).expand_as(vq) / math.sqrt(float(vq.shape[-1]))  
        softmax_vq = vs.softmax(dim=-2)
        dropout_vq = torch.nn.functional.dropout(softmax_vq, p=dropout_p)
        return dropout_vq.matmul(value)
# Initializing the model
m = Model()


x1 = torch.randn(100000, 64)
x2 = torch.randn(100000, 8)
